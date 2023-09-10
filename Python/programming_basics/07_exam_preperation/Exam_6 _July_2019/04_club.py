profit = float(input())

money_won = 0

while money_won <= profit:
    name_of_cocktail = input()

    if name_of_cocktail == 'Party!':
        break

    number_of_cocktails = int(input())

    current_amount = len(name_of_cocktail) * number_of_cocktails

    if current_amount % 2 != 0:
        current_amount -= current_amount * 0.25

    money_won += current_amount

if money_won >= profit :
    print('Target acquired.')
else:
    print(f'We need {(profit - money_won):.2f} leva more.')

print(f'Club income - {money_won:.2f} leva.')