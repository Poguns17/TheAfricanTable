from flask import Flask, render_template, url_for, redirect, request, flash, session
from data import country_data
import random
app = Flask(__name__)

app.secret_key = "table"


@app.route("/")
def home():
    preview_countries = list(country_data.keys())[:5]
    return render_template("index.html", preview_countries=preview_countries)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/countries/")
def countries():
    return render_template("countries.html", countries=list(country_data.keys()))


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
