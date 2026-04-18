import datetime
from flask import Flask, render_template, current_app

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/blog/")
def blog():
    current_year = datetime.datetime.now().strftime("%Y")
    return render_template("blog.html")


@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")


if __name__ == "__main__":
    app.run()