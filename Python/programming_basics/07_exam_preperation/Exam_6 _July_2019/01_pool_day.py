from  math import  ceil

number_of_people = int(input())
fee = float(input())
price_for_lounger = float(input())
price_for_umbrella = float(input())

total_price = (number_of_people * fee + ceil(number_of_people / 2) * price_for_umbrella + ceil(number_of_people * 0.75) *
               price_for_lounger)

print (f'{total_price:.2f} lv.')