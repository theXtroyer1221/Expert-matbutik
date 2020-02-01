import json

with open("json/product.json", "r", encoding='utf8') as f:
    product_list = json.load(f)

print(product_list["Chark"][0]["namn"])
for product in product_list:
    print(product)
print("-----")
#for i in range(len(product_list)):
#    for j in product_list[i]:
#        print(j["namn"])
print(product_list)