annual_training_fee = int(input())

shoes = annual_training_fee - (annual_training_fee * 0.4)
clothes = shoes - (shoes * 0.2)
ball = clothes / 4
accessories = ball / 5

total_price_for_equipment = shoes + clothes + ball + accessories

total_price = total_price_for_equipment + annual_training_fee

print(total_price)