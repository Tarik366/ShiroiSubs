from flask import Flask, render_template, request, url_for, redirect
from itsdangerous import Signer, BadSignature
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html")


@app.route("/main/<name>")
def homen(name):
    if name.lower() == "Tarık":
        return redirect(url_for("Tarık"))
    return render_template("main.html", username=name)


@app.route("/seriler")
def seriler():
    return render_template("seriler.html")


@app.route("/yeniler")
def yeniler():
    return render_template("Yeniler.html")


@app.route("/duyuru")
def duyuru():
    return render_template("Duyurular.html")


@app.route("/devam")
def devam():
    return render_template("DevamEdenler.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        return redirect(url_for("homen", name=username))
    else:
        return render_template("Login/login.html")


@app.route("/main/Tarık")
def Admin():
    return render_template("v55byo0k29.html")


@app.route("/yeni-bolum", methods=["GET", "POST"])
def uploadnewepisode():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            print(image)
    return render_template("BolumYukle.html")

@app.route("/02273")
def manga():
    return render_template("Seriler/Abandoned Wife Has a New Husband/AbandonedWifeHasaNewHusband.html")
@app.route("/98637")
def Amerika():
    return render_template("Seriler/AmericanWeebinJapan/AmericanWeebinJapan.html")