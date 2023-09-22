from flask import Flask, request, render_template


app = Flask("__name__")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def calc():
    peso = int(request.form["weight"])
    altura = float(request.form["height"])
    imc = peso / (altura**2)
    return render_template("resultado.html", imc = str(f'{imc:.2f}'))
    