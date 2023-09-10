drink = input()
sugar = input()
number_of_drinks = int(input())

total_price = 0

if drink == 'Espresso':
    if sugar == 'Without':
        total_price = number_of_drinks * 0.9
        total_price -= total_price * 0.35
    elif sugar == 'Normal':
        total_price = number_of_drinks
    elif sugar == 'Extra':
        total_price = number_of_drinks * 1.2

    if number_of_drinks >= 5:
        total_price -= total_price * 0.25

elif drink == 'Cappuccino':
    if sugar == 'Without':
        total_price = number_of_drinks
        total_price -= total_price * 0.35
    elif sugar == 'Normal':
        total_price = number_of_drinks * 1.2
    elif sugar == 'Extra':
        total_price = number_of_drinks * 1.6

elif drink == 'Tea':
    if sugar == 'Without':
        total_price = number_of_drinks * 0.5
        total_price -= total_price * 0.35
    elif sugar == 'Normal':
        total_price = number_of_drinks * 0.6
    elif sugar == 'Extra':
        total_price = number_of_drinks * 0.7

if total_price > 15:
    total_price -= total_price * 0.2

print(f'You bought {number_of_drinks} cups of {drink} for {total_price:.2f} lv.')