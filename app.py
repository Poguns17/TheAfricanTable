from flask import Flask,url_for, render_template
app = Flask(__name__)


@app.route("/")
def home():
    image_url = url_for('static', filename='img/logo.png')
    return render_template("index.html", image=image_url)
