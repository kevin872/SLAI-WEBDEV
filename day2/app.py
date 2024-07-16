from data_exp import read_csv
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/<int:num>")
def details(num):
    data = read_csv("pokemon.csv")
    return [pokemon for pokemon in data if int(pokemon["#"]) == num]