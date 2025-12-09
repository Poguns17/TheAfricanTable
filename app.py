from flask import Flask, url_for, render_template
from data import country_data
import random
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


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
    return render_template("country.html", country=country, data=country_info)