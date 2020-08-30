import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cpi")
def cpi():
    return render_template("cpi.html")


@app.route("/inflation")
def inflation():
    return render_template("inflation.html")


@app.route("/wages")
def wages():
    return render_template("wages.html")


@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

@app.route("/ML")
def ML():
    return render_template("ML.html")

@app.route("/data")
def data():
    return render_template("data.html")


if __name__ == "__main__":
    app.run(debug=True)