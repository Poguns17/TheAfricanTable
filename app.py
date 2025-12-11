from flask import Flask, render_template, url_for, redirect, request, flash, session
from data import country_data
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import random, json, os
from models import db, Country, Recipe, QuizQuestion, User

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///africantable.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

app.secret_key = "table"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# sign up and login
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"].strip().lower()
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        # Check existing user
        if User.query.filter((User.username == username) | (User.email == email)).first():
            flash("Username or email already exists")
            return redirect(url_for("signup"))

        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        login_user(user)
        return redirect(url_for("home"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip().lower()
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            flash("Invalid username or password")
            return redirect(url_for("login"))

        login_user(user)
        return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


# home page
@app.route("/")
def home():
    preview_countries = Country.query.limit(5).all()
    return render_template("index.html", preview_countries=preview_countries)


# about page
@app.route("/about/")
def about():
    return render_template("about.html")


# countries list page
@app.route("/countries/")
def countries():
    countries = Country.query.order_by(Country.name).all()
    return render_template("countries.html", countries=countries)


# countries
@app.route("/country/<country>")
def country_page(country):
    country_obj = Country.query.filter(Country.name.ilike(country)).first_or_404()
    recipes = Recipe.query.filter_by(country_id=country_obj.id).all()

    # Group by category
    recipes_by_category = {}
    for r in recipes:
        recipes_by_category.setdefault(r.category, []).append(r)

    # Count quiz questions
    quiz_length = QuizQuestion.query.filter_by(country_id=country_obj.id).count()

    return render_template("country.html", country=country_obj, description=country_obj.description, recipes_by_category=recipes_by_category, quiz_length=quiz_length)


# get random recipe on country page
@app.route("/country/<country>/random")
def random_recipe_from_country(country):
    country_obj = Country.query.filter_by(name=country.lower()).first_or_404()
    recipes = Recipe.query.filter_by(country_id=country_obj.id).all()

    if not recipes:
        flash("No recipes found for this country")
        return redirect(url_for("country_page", country=country))

    chosen_recipe = random.choice(recipes)
    return redirect(url_for("recipe_page", country=country_obj.name, recipe_name=chosen_recipe.name.lower().replace(" ", "-")))


# recipes
@app.route("/country/<country>/recipe/<recipe_name>")
def recipe_page(country, recipe_name):
    country_obj = Country.query.filter(Country.name.ilike(country.lower())).first_or_404()
    recipe_name_clean = recipe_name.replace("-", " ").strip()
    recipe = Recipe.query.filter(
        Recipe.name.ilike(recipe_name_clean),
        Recipe.country_id == country_obj.id
    ).first_or_404()

    # Convert JSON → Python lists
    recipe.ingredients = json.loads(recipe.ingredients)
    recipe.instructions = json.loads(recipe.instructions)

    return render_template("recipes.html", country=country_obj, recipe=recipe)


# helper to prepare questions
def prepare_quiz_questions(country_id):
    questions = QuizQuestion.query.filter_by(country_id=country_id).all()
    random.shuffle(questions)

    # Parse options + answer JSON
    for q in questions:
        try:
            q.options = json.loads(q.options)
        except:
            q.options = []
        try:
            q.answer = json.loads(q.answer)
        except:
            pass
    return questions


# country quiz on the country page
@app.route("/country/<country>/quiz", methods=["GET", "POST"])
def country_quiz(country):
    # Get the Country object (case-insensitive)
    country_obj = Country.query.filter(Country.name.ilike(country.lower())).first_or_404()
    session_key = f"quiz_{country_obj.id}_state"

    # Initialize quiz if first visit or restart
    if session_key not in session or (request.method == "GET" and "restart" in request.args):
        questions = QuizQuestion.query.filter_by(country_id=country_obj.id).all()
        if not questions:
            return "No quiz found for this country", 404

        # Store question IDs in session
        question_ids = [q.id for q in questions]
        random.shuffle(question_ids)

        session[session_key] = {
            "index": 0,
            "questions": [q.id for q in questions],
            "answers": []
        }

    state = session.get(session_key)
    idx = state["index"]
    total = len(state["questions"])

    # Handle POST: user submitted an answer
    if request.method == "POST":
        current_q_id = state["questions"][idx]
        current_q = QuizQuestion.query.get(current_q_id)
        # Parse stored JSON
        try:
            correct_answer = json.loads(current_q.answer)
        except:
            correct_answer = current_q.answer
        user_answer = request.form.get("answer")

        # Normalize True/False answers
        if current_q.type == "tf":
            user_answer = True if user_answer == "True" else False

        # Record answer
        state["answers"].append({
            "question": current_q.question,
            "correct_answer": correct_answer,
            "user_answer": user_answer,
            "correct": user_answer == correct_answer
        })

        # Advance to next question
        state["index"] = idx + 1
        session[session_key] = state

    # Refresh state after POST
    state = session.get(session_key)
    idx = state["index"]

    # End of quiz → show results
    if state["index"] >= total:
        answers = state["answers"]
        score = sum(1 for a in answers if a["correct"])

        session.pop(session_key)
        return render_template(
            "quiz-result.html",
            country=country_obj,
            total=total,
            score=score,
            results=answers
        )

    # Show current question
    current_q = QuizQuestion.query.get(state["questions"][state["index"]])
    # Parse options
    try:
        current_q.options = json.loads(current_q.options)
    except:
        current_q.options = []

    qnum = state["index"] + 1
    return render_template(
        "quiz.html",
        country=country_obj,
        question=current_q,
        qnum=qnum,
        total=total
    )


# randomiser page
@app.route("/randomizer", methods=["GET", "POST"])
def randomizer():
    category_options = db.session.query(Recipe.category).distinct().all()
    category_options = sorted([c[0] for c in category_options if c[0]])

    if request.method == "POST":
        choice_type = request.form.get("choice_type")
        selected_category = request.form.get("category")

        if choice_type == "country":
            country_obj = random.choice(Country.query.all())
            return redirect(url_for("country_page", country=country_obj.name))

        elif choice_type == "recipe":
            filtered_recipes = Recipe.query
            if selected_category:
                filtered_recipes = filtered_recipes.filter_by(category=selected_category)
            filtered_recipes = filtered_recipes.all()

            if not filtered_recipes:
                flash(f"No recipes found in category '{selected_category}'")
                return redirect(url_for("randomizer"))

            chosen_recipe = random.choice(filtered_recipes)
            return redirect(url_for(
                "recipe_page",
                country=chosen_recipe.country.name,
                recipe_name=chosen_recipe.name.lower().replace(" ", "-")
            ))

    return render_template("randomiser.html", category_options=category_options)


# error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", code=404, title="Page Not Found", message="Oops! The page you were looking for doesn't exist."), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("error.html", code=500, title="Server Error", message="Something went wrong on our end. Please try again later."), 500


# temporary test route
@app.route("/create-db")
def create_db():
    db.create_all()
    return "Database created!"

