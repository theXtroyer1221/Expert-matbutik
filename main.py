from flask import Flask, render_template

import json
import random

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


if __name__ == "__main__":
    app.run()
