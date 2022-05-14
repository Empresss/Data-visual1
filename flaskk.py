from operator import index
from flask import Flask, render_template
from flask_sqlalchemy import SignallingSession
import pandas as pd


app = Flask(__name__)


@app.route("/tables")
def heyy():
    df = pd.read_excel("static/Cleaned.xlsx")

    return render_template("view.html")


@app.route("/")
def homepage():
    return "<h1>Thy homepage</h1>"


if __name__ == "__main__":
    app.run(debug=True)
