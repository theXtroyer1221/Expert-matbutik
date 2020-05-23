from flask import Flask, render_template, request
from forms import SignUpForm

import json
import random

import smtplib

app = Flask(__name__)
app.config["SECRET_KEY"] = "ExpertMatbutik"
app.config["TEMPLATES_AUTO_RELOAD"] = True

with open("json/week-rea.json", "r", encoding='utf8') as f:
    week_rea = json.load(f)


def send_mail(name, mail, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login("jaddou2005@gmail.com", "wccjxrgoffwxmulu")
    except Exception as e:
        print(e)

    subject = "Ett medelande fron kund(kontakta oss)"
    body = f"Kundens namn: '{name}'\n epost: '{mail}'\n\n meddelande: {message}"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail("jaddou2005@gmail.com", "alnabki@yahoo.com", msg)

    server.quit()

    print("* Email sent")


@app.route("/", methods=["GET", "POST"])
def index():
    form = SignUpForm()
    if request.method == "POST":
        result = request.form
        name = result["name"].encode('utf-8')
        mail = result.get("mail").encode('utf-8')
        message = result["message"].encode('utf-8')

        send_mail(name, mail, message)

    product = ["eid", "store", "grön", "livsmedel", "paket"]

    return render_template("index.html",
                           len=len(product),
                           product_image=product,
                           erbjudan=week_rea["product"],
                           form=form)


@app.route("/varor")
def varor():
    with open("json/product.json", "r", encoding='utf8') as f:
        product = json.load(f)

    return render_template("product.html", product=product)


@app.route("/paket")
def paket():
    return render_template("paket.html")


@app.route("/ramadan")
def ramadan():
    return render_template("ramadan.html")


if __name__ == "__main__":
    app.run(debug=True)
