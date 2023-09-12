energy = 100
coins = 100
events_list = input().split('|')

for arg in events_list:
    arg = arg.split('-')
    event = arg[0]
    number = int(arg[1])

    if event == 'rest':
        energy += number
        if energy > 100:
            number -= energy - 100
            energy = 100
        print(f'You gained {number} energy.')
        print(f'Current energy: {energy}.')
    elif event == 'order':
        if energy >= 30:
            energy -= 30
            coins += number
            print(f'You earned {number} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins >= number:
            coins -= number
            print(f'You bought {event}.')
        else:
            print(f'Closed! Cannot afford {event}.')
            break
else:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
