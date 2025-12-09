from flask import Flask, url_for, render_template
from data import country_data
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
