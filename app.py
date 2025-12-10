from flask import Flask, render_template, url_for, redirect, request, flash, session
from data import country_data
import random
import os
from flask_sqlalchemy import SQLAlchemy
from models import db, Country, Recipe, QuizQuestion

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///africantable.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.secret_key = "table"


# home page
@app.route("/")
def home():
    preview_countries = list(country_data.keys())[:5]
    return render_template("index.html", preview_countries=preview_countries)


# about page
@app.route("/about/")
def about():
    return render_template("about.html")


# countries list page
@app.route("/countries/")
def countries():
    return render_template("countries.html", countries=list(country_data.keys()))


# countries
@app.route("/country/<country>")
def country_page(country):
    country_info = country_data.get(country.lower())
    if not country_info:
        return "Country not found", 404

    description = country_info.get("description", "")
    recipes_by_category = country_info.get("recipes", {})

    return render_template(
        "country.html",
        country=country,
        description=description,
        data=country_info,
        recipes=recipes_by_category,
        recipes_by_category=recipes_by_category
    )


# get random recipe on country page
@app.route("/country/<country>/random")
def random_recipe_from_country(country):
    country_info = country_data.get(country.lower())
    if not country_info:
        return "Country not found", 404

    # Flatten all recipe categories into one list
    all_recipes = []
    for category, recipe_list in country_info["recipes"].items():
        all_recipes.extend(recipe_list)

    # Randomly pick one recipe
    chosen_recipe = random.choice(all_recipes)

    # Redirect to recipe page
    return redirect(url_for("recipe_page", country=country, recipe_name=chosen_recipe["name"]))


# recipes
@app.route("/country/<country>/recipe/<recipe_name>")
def recipe_page(country, recipe_name):
    country_info = country_data.get(country.lower())
    if not country_info:
        return "Country not found", 404

    recipes_by_category = country_info.get("recipes", {})

    # Search for recipe in country's categories
    for category, recipe_list in country_info["recipes"].items():
        for recipe in recipe_list:
            if recipe["name"].lower().replace(" ", "-") == recipe_name.lower().replace(" ", "-"):
                return render_template("recipes.html", recipe=recipe, country=country)

    return "Recipe not found", 404


# helper to make a shallow serializable question list
def prepare_quiz_questions(country_key):
    country_info = country_data.get(country_key)
    if not country_info:
        return None
    # create list of question dicts
    questions = []
    for q in country_info.get("quiz", []):
        questions.append(q.copy())
    random.shuffle(questions)
    return questions


# country quiz on the country page
@app.route("/country/<country>/quiz", methods=["GET", "POST"])
def country_quiz(country):
    key = country.lower()
    country_info = country_data.get(key)
    if not country_info:
        return "Country not found", 404

    session_key = f"quiz_{key}_state"

    # On first GET or if session doesn't have quiz state, initialize
    if session_key not in session or request.method == "GET" and 'restart' in request.args:
        questions = prepare_quiz_questions(key)
        if questions is None:
            return "No quiz found for this country", 404
        # store: index, questions, user_answers list
        session[session_key] = {
            "index": 0,
            "questions": questions,
            "answers": []
        }

    state = session.get(session_key)

    # POST: user submitted an answer to current question
    if request.method == "POST":
        # fetch submitted answer (for mcq: 'choice', for tf: 'tf_choice')
        current_index = state["index"]
        q = state["questions"][current_index]
        user_answer = request.form.get("answer", None)
        # normalize boolean answers for tf
        if q["type"] == "tf":
            # user will submit "True" or "False"
            user_answer = True if user_answer == "True" else False
        # record answer
        state["answers"].append({
            "question": q["question"],
            "correct": q["answer"],
            "given": user_answer,
            "type": q["type"]
        })
        # advance
        state["index"] = current_index + 1
        session[session_key] = state  # save back

    # Get updated state
    state = session.get(session_key)
    idx = state["index"]
    total = len(state["questions"])

    # If finished: compute score and show results
    if idx >= total:
        answers = state["answers"]
        score = 0
        for a in answers:
            # normalize correct/given for comparison
            correct = a["correct"]
            given = a["given"]
            if isinstance(correct, bool):
                if given is True or given is False:
                    if given == correct:
                        score += 1
            else:
                # string compare (case-insensitive)
                if isinstance(given, str) and given.strip().lower() == str(correct).strip().lower():
                    score += 1
        # save results when db is implemented
        # Clear session state for this quiz
        session.pop(session_key, None)
        return render_template("quiz-result.html", country=country, total=total, score=score, answers=answers)

    # Not finished: show current question
    current_q = state["questions"][idx]
    qnum = idx + 1
    return render_template("quiz.html", country=country, question=current_q, qnum=qnum, total=total)


# randomiser page
@app.route("/randomizer", methods=["GET", "POST"])
def randomizer():
    category_options = set()
    # Collect all categories from all countries for the form dropdown
    for country_info in country_data.values():
        for cat in country_info.get("recipes", {}).keys():
            category_options.add(cat)
    category_options = sorted(category_options)

    selected_category = None
    result = None

    if request.method == "POST":
        choice_type = request.form.get("choice_type")
        selected_category = request.form.get("category")

        if choice_type == "country":
            # Randomly pick a country
            result = random.choice(list(country_data.keys()))
            # Redirect to that country's page
            return redirect(url_for("country_page", country=result))

        elif choice_type == "recipe":
            # Filter recipes by selected category
            filtered_recipes = []
            for country, info in country_data.items():
                recipes = info.get("recipes", {})
                if selected_category in recipes:
                    for recipe in recipes[selected_category]:
                        # Include country for redirect later
                        recipe_copy = recipe.copy()
                        recipe_copy["country"] = country
                        filtered_recipes.append(recipe_copy)

            if not filtered_recipes:
                flash(f"No recipes found in category '{selected_category}'")
                return redirect(url_for("randomizer"))

            # Pick random recipe
            chosen_recipe = random.choice(filtered_recipes)
            recipe_slug = chosen_recipe["name"].lower().replace(" ", "-")
            return redirect(url_for("recipe_page", country=chosen_recipe["country"], recipe_name=recipe_slug))

    return render_template(
        "randomiser.html", category_options=category_options, selected_category=selected_category)


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

