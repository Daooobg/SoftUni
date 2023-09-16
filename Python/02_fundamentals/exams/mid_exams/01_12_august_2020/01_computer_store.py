input_line = input()

total_price_without = 0
total_taxes = 0

while input_line != 'special' and input_line != 'regular':
    current_price = float(input_line)

    if current_price > 0:
        total_price_without += current_price
        total_taxes += current_price * 0.2
    else:
        print('Invalid price!')

    input_line = input()

if total_price_without == 0:
    print('Invalid order!')
else:
    print('Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {total_price_without:.2f}$')
    print(f'Taxes: {total_taxes:.2f}$')
    print('-----------')
    total_price = total_price_without + total_taxes
    if input_line == 'special':
        total_price -= total_price * 0.1

    print(f'Total price: {total_price:.2f}$')