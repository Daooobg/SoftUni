type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())

price = 0

if type_of_flowers == 'Roses':
    price = number_of_flowers * 5
    if number_of_flowers > 80:
        price = price - (price * 0.1)
elif type_of_flowers == 'Dahlias':
    price = number_of_flowers * 3.8
    if number_of_flowers > 90:
        price = price - (price * 0.15)
elif type_of_flowers == 'Tulips':
    price = number_of_flowers * 2.8
    if number_of_flowers > 80:
        price = price - (price * 0.15)
elif type_of_flowers == 'Narcissus':
    price = number_of_flowers * 3
    if number_of_flowers < 120:
        price = price * 1.15
elif type_of_flowers == 'Gladiolus':
    price = number_of_flowers * 2.5
    if number_of_flowers < 80:
        price = price * 1.2

if budget >= price :
    print(f'Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {(budget - price):.2f} leva left.')
else:
    print(f'Not enough money, you need {(price - budget):.2f} leva more.')