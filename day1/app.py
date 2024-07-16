from data_exp import read_csv
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

# def why(pokemon):
#     if int(list(pokemon.values())[0]) == num

@app.route("/<int:num>")
def details(num):
    data = read_csv("pokemon.csv")
    for pokemon in data:
        if int(list(pokemon.values())[0]) == num:
            return pokemon
        
    
    return ""