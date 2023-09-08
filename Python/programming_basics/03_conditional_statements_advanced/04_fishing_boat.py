budget = int(input())
season = input()
number_of_fishermen = int(input())

total_price = 0

if season == 'Spring':
    total_price = 3000
elif season == 'Summer' or season == 'Autumn':
    total_price = 4200
elif season == 'Winter':
    total_price = 2600

if number_of_fishermen <= 6:
    total_price -=total_price * 0.1
elif number_of_fishermen <= 11:
    total_price -=total_price * 0.15
else:
    total_price -= total_price * 0.25

if season != 'Autumn' and number_of_fishermen % 2 == 0:
    total_price -= total_price * 0.05

if budget >= total_price:
    print(f'Yes! You have {(budget - total_price):.2f} leva left.')
else:
    print(f'Not enough money! You need {(total_price - budget):.2f} leva.')