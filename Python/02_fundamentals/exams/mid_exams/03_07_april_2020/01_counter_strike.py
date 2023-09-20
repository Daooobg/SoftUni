energy = int(input())

input_line = input()
won_battles = 0

while input_line != 'End of battle':
    distance = int(input_line)
    if energy - distance < 0:
        print(f'Not enough energy! Game ends with {won_battles} won battles and {energy} energy')
        break

    energy -= distance
    won_battles += 1


    if won_battles % 3 == 0:
        energy += won_battles

    input_line = input()

else:
    print(f'Won battles: {won_battles}. Energy left: {energy}')