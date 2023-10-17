def shop_from_grocery_list(budget, grocery_list, *args):

    bought_products = set()
    grocery_list = set(grocery_list)

    for product_name, price in args:
        if budget < price:
            break

        if product_name not in grocery_list:
            continue

        if product_name in bought_products:
            continue

        bought_products.add(product_name)
        budget -= price

    difference = grocery_list.difference(bought_products)

    result = ''
    if difference:
        result = f"You did not buy all the products. Missing products: {', '.join(difference)}."
    else:
        result = f"Shopping is successful. Remaining budget: {budget:.2f}."

    return result

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
