from data_exp import read_csv
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    data = read_csv("pokemon.csv")
    return render_template("index.html", data=data)

@app.route("/<int:num>")
def details(num):
    data = read_csv("pokemon.csv")
    return [pokemon for pokemon in data if int(pokemon["#"]) == num]
