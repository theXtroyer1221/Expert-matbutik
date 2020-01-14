import json
from art import *


class App:
    def intro(self):
        Art = text2art("Database")
        tprint("Database")
        print("__" * 25)

        print("running weekly offers in database...")
        print("")

    def Main(self):
        with open("json/week-rea.json", "r") as f:
            product_list = json.load(f)

        print("all offer names")
        for producto in product_list:
            print(producto["name"])


App.intro(App)
App.Main(App)