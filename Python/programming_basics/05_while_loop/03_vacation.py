money_for_tour = float(input())
available_money = float(input())

days_counter = 0
spending_days_counter = 0

while money_for_tour > available_money and spending_days_counter < 5:
    command = input()
    current_amount = float(input())
    days_counter += 1
    if command == 'spend':
        available_money -= current_amount
        spending_days_counter += 1
        if available_money < 0:
            available_money = 0
    elif command == 'save':
        available_money += current_amount
        spending_days_counter = 0


if spending_days_counter == 5:
    print('You can\'t save the money.')
    print(days_counter)
else:
    print(f'You saved the money for {days_counter} days.')