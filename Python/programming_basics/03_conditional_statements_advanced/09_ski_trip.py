days_to_stay = int(input())
type_of_room = input()
review = input()

nights = days_to_stay - 1

total_price = 0

if type_of_room == 'room for one person':
    total_price = nights * 18

elif type_of_room == 'apartment':
    total_price = nights * 25

    if days_to_stay < 10:
        total_price -= total_price * 0.3
    elif days_to_stay <= 15:
        total_price -= total_price * 0.35
    else:
        total_price -= total_price * 0.5

elif type_of_room == 'president apartment':
    total_price = nights * 35

    if days_to_stay < 10:
        total_price -= total_price * 0.1
    elif days_to_stay <= 15:
        total_price -= total_price * 0.15
    else:
        total_price -= total_price * 0.2

if review == 'positive':
    total_price = total_price * 1.25
elif review == 'negative':
    total_price -= total_price * 0.1


print(f'{total_price:.2f}')