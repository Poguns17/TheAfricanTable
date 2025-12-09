from flask import Flask, render_template, url_for, redirect
from data import country_data
import random
app = Flask(__name__)


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

    description = country_info["description"]
    recipes = country_info["recipes"]

    return render_template("country.html", country=country, data=country_info, description=description, recipes=recipes)


@app.route("/country/<country>/recipe/<recipe_name>")
def recipe_page(country, recipe_name):
    country_info = country_data.get(country.lower())
    if not country_info:
        return "Country not found", 404

    for category, recipe_list in country_info["recipes"].items():
        for recipe in recipe_list:
            if recipe["name"].lower() == recipe_name.lower():
                return render_template(
                    "recipes.html", country=country, recipe=recipe, category=category)

    return "Recipe not found", 404

