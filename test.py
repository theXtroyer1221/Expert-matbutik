import json

with open("json/week-rea.json", "r") as f:
    product_list = json.load(f)

if product_list["name"] == None:
    print("lolololo")
