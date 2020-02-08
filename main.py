from flask import Flask, render_template

import json
import random
import request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

with open("json/week-rea.json", "r", encoding='utf8') as f:
    week_rea = json.load(f)


@app.route("/")
def index():
    product = ["store", "sattelite", "unicorn", "paket"]
    return render_template("index.html",
                           len=len(product),
                           product_image=product,
                           erbjudan=week_rea["product"])


@app.route("/varor")
def varor():
    with open("json/product.json", "r", encoding='utf8') as f:
        product = json.load(f)

    return render_template("product.html", product=product)


@app.route("/paket")
def paket():
    return render_template("paket.html")


if __name__ == "__main__":
    app.run(debug=True)
