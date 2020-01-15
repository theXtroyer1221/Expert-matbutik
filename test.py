import json

with open("json/week-rea.json", "r") as f:
    product_list = json.load(f)

for product in product_list[1]:
    print(product)
