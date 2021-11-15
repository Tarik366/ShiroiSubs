from flask import Flask, render_template, request, url_for, redirect
from itsdangerous import Signer, BadSignature
import random
import os

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
def admin():
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
def american():
    return render_template("Seriler/AmericanWeebInJapan/AmericanWeebinJapan.html")


@app.route("/60078")
def mother():
    return render_template("Seriler/AMotherInHer30SLikeMeIsAlright/AMotherInHer30SLikeMeIsAlright.html")


@app.route("/36531")
def night():
    return render_template("Seriler/ANightTheEmperor/ANightTheEmperor.html")


@app.route("/98637")
def bakapple():
    return render_template("Seriler/Bakapple/Bakapple.html")


@app.route("/55019")
def dragon():
    return render_template("Seriler/DragonRaisingManual/DragonRaisingManual.html")


@app.route("/83410")
def iceguy():
    return render_template("Seriler/IceGuyAndTheCoolFemaleColleague/IceGuyAndTheCoolFemaleColleague.html")


@app.route("/81853")
def beat():
    return render_template("Seriler/IOnlyWantBeatYou/IOnlyWantToBeatYou.html")


@app.route("/97141")
def meme():
    return render_template("Seriler/MemeGirls/MemeGirls.html")


@app.route("/10373")
def roommate():
    return render_template("Seriler/MyRoommateIsntFromThisWorld/MyRoommateIsntFromThisWorld.html")


@app.route("/30034")
def osana():
    return render_template("Seriler/OsananajiminiNajimitai/OsananajiminiNajimitai.html")


@app.route("/37130")
def shiwa():
    return render_template("Seriler/Shiwa/Shiwa.html")


@app.route("/01582")
def shukan():
    return render_template("Seriler/ShukanBrick/ShukanBrick.html")


@app.route("/84269")
def sunshine():
    return render_template("Seriler/SunshineDoll/SunshineDoll.html")


@app.route("/61897")
def take():
    return render_template("Seriler/TakeMeOut/TakeMeOut.html")


@app.route("/83905")
def tekito():
    return render_template("Seriler/TekitonaMaid/TekitonaMaid.html")


@app.route("/36560")
def fox():
    return render_template("Seriler/TheFoxsTrap/TheFoxsTrap.html")


@app.route("/61772")
def onee():
    return render_template("Seriler/Oneesan/Oneesan.html")


@app.route("/21262")
def today():
    return render_template("Seriler/TodayLivingWithYou/TodayLivingWithYou.html")


"""
@app.route("/10666")
def American():
    return render_template("Seriler/")


@app.route("/91154")
def American():
    return render_template("Seriler/")


@app.route("/80225")
def American():
    return render_template("Seriler/")


"""