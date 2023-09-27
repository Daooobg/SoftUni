import re

input_line = input()

pattern = r'>>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)'
products = []
total_sum = 0

while input_line != 'Purchase':
    match = re.search(pattern, input_line)
    if match:
        furniture, price, quantity = match.groups()

        products.append(furniture)
        total_sum += float(price) * int(quantity)

    input_line = input()

print('Bought furniture:')
for product in products:
    print(product)
print(f'Total money spend: {total_sum:.2f}')