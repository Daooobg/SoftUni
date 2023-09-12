items_list = input().split('|')
budget = float(input())

price_list = []
sum_price = 0
total_sold_price = 0

for arg in items_list:
    arg = arg.split('->')
    current_item = arg[0]
    current_price = float(arg[1])

    if budget < current_price:
        continue

    if current_item == 'Clothes':
        if current_price <= 50:
            price_list.append(current_price)
            budget -= current_price
    elif current_item == 'Shoes':
        if current_price <= 35:
            price_list.append(current_price)
            budget -= current_price
    elif current_item == 'Accessories':
        if current_price <= 20.5:
            price_list.append(current_price)
            budget -= current_price


for price in price_list:
    sum_price += price
    total_sold_price += price * 1.4
    print(f'{(price * 1.4):.2f}', end=' ')
print()
print(f'Profit: {(total_sold_price - sum_price):.2f}')
if total_sold_price + budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
# 120
# Shoes->41.20|Clothes->20.30|Accessories->40|Shoes->15.60|Shoes->33.30|Clothes->48.60
# 90
