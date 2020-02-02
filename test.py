import json

with open("json/product.json", "r", encoding='utf8') as f:
    product_list = json.load(f)

for product in product_list:
    for i in product_list[product]:
        print(i)
