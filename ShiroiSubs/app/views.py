import os
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("main.html")


@app.route("/main/<name>")
def homen(name):
    if name.lower() == "Tarık":
        return redirect(url_for("Tarık"))
    return render_template("main.html", username=name)


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


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/yeni-bolum")
def neu():
    return render_template("BolumYukle.html")


@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("bolum-tamam.html")


if __name__ == "__main__":
    app.run(port=4555, debug=True)


# Seriler
@app.route("/02273")
def abandoned():
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


@app.route("/98639")
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


@app.route("/26475")
def ao():
    return render_template("Seriler/AoNoHako.html")


@app.route("/64685")
def tennen():
    return render_template("Tags/tennen.html")


@app.route("/77374")
def live():
    return render_template("Seriler/PleaseDontLivestreamIt/PleaseDontLivestreamIt.html")

# Etiketler
@app.route("/4517")
def comedy():
    return render_template("Tags/Comedy.html")


@app.route("/2463")
def drama():
    return render_template("Tags/Drama.html")


@app.route("/5994")
def fantasy():
    return render_template("Tags/Fantasy.html")


@app.route("/9867")
def manga():
    return render_template("Tags/Manga.html")


@app.route("/5922")
def manwha():
    return render_template("Tags/Manwha.html")


@app.route("/7125")
def manhua():
    return render_template("Tags/Manhua.html")


@app.route("/5041")
def romance():
    return render_template("Tags/Romance.html")


@app.route("/5197")
def shoujo():
    return render_template("Tags/Shoujo.html")


@app.route("/8459")
def shounen():
    return render_template("Tags/Shounen.html")


@app.route("/0529")
def sulice():
    return render_template("Tags/SliceOfLife.html")


@app.route("/9953")
def tragedy():
    return render_template("Tags/Tragedy.html")


@app.route("/3783")
def school():
    return render_template("Tags/SchoolLife.html")


@app.route("/8114")
def isekai():
    return render_template("Tags/isekai.html")


@app.route("/5057")
def magic():
    return render_template("Tags/magic.html")


@app.route("/1302")
def demon():
    return render_template("Tags/demon.html")


@app.route("/6489")
def ecchi():
    return render_template("Tags/ecchi.html")


@app.route("/1957")
def horror():
    return render_template("Tags/horror.html")


@app.route("/1675")
def supernatural():
    return render_template("Tags/supernatural.html")


@app.route("/4646")
def spor():
    return render_template("Tags/spor.html")


@app.route("/1675")
def action():
    return render_template("Tags/action.html")


@app.route("/1598")
def macera():
    return render_template("Tags/adventure.html")