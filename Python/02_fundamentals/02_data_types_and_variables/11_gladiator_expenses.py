lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
number_of_shield_breaks = 0

for current_lost in range(1, lost_fights + 1):
    if current_lost % 2 == 0:
        expenses += helmet_price
    if current_lost % 3 == 0:
        expenses += sword_price
        if current_lost % 2 == 0:
            expenses += shield_price
            number_of_shield_breaks += 1
            if number_of_shield_breaks % 2 == 0:
                expenses += armor_price


print(f'Gladiator expenses: {expenses:.2f} aureus')