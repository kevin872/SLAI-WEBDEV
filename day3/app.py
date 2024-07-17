from data_exp import read_csv
from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)
    app.data = read_csv("pokemon.csv")
    types = set()
    for pokemon in app.data:
        types.add(pokemon["Type 1"])
        if pokemon["Type 2"]:
            types.add(pokemon["Type 2"])
    app.types = sorted(types)
    return app

app = create_app()


@app.route("/")
def index():
    # return render_template("index.html", data=data)
    return render_template("query_form.html", types=app.types)

@app.post("/")
def index_post():
    question = request.form
    data = query(app.data, question)
    return render_template("index.html", data=data)

def query(data, question):
    result = []
    # print(question.getlist(0))
    for item in data:
        if (item["Type 1"] != question['type'] or item["Type 2"] == '') and item["Type 2"] != question['type']:
            continue
        if item["Legendary"] != True and 'legendary' in question:
            continue
        if question["max_HP"] != '':
            if int(question["max_HP"]) < item["HP"]:
                continue
        if question["min_HP"] != '':
            if int(question["min_HP"]) > item["HP"]:
                continue
        result.append(item)
    return result

@app.route("/<int:num>")
def details(num):
    return [pokemon for pokemon in app.data if int(pokemon["#"]) == num]

