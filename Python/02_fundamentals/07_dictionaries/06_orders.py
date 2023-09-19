order = {}

input_line = input()

while input_line != 'buy':
    current_product, current_price, current_quantity = input_line.split()
    current_price = float(current_price)
    current_quantity = int(current_quantity)

    if current_product in order.keys():
        if order[current_product]['price'] != current_price:
            order[current_product]['price'] = current_price

        order[current_product]['quantity'] += current_quantity

    else:
        order[current_product] = {}
        order[current_product]['price'] = current_price
        order[current_product]['quantity'] = current_quantity

    input_line = input()

for k, i in order.items():
    print(f"{k} -> {(i['price'] * i['quantity']):.2f}")