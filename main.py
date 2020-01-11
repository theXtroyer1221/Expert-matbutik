from flask import Flask, render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    product = ["apple", "banana", "product1", "product2", "orange"]
    return render_template("index.html",
                           len=len(product),
                           product_image=product)


if __name__ == "__main__":
    app.run()
