month = input()
number_of_days = int(input())

studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = number_of_days * 50
    apartment_price = number_of_days * 65

    if 7 < number_of_days <= 14:
        studio_price -= studio_price * 0.05
    elif number_of_days > 14:
        studio_price -= studio_price * 0.3

elif month == 'June' or month == 'September':
    studio_price = number_of_days * 75.2
    apartment_price = number_of_days * 68.7

    if number_of_days > 14:
        studio_price -= studio_price * 0.2

elif month == 'July' or month == 'August':
    studio_price = number_of_days * 76
    apartment_price = number_of_days * 77

if number_of_days > 14:
    apartment_price -= apartment_price * 0.1

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')