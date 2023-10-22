fishing_area_size = int(input())

fishing_area = []
ship_coord = ()
collected_fishes = 0

movements = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(fishing_area_size):
    curr_row = [char for char in input()]
    fishing_area.append(curr_row)

    if 'S' in curr_row:
        ship_coord = (row, curr_row.index('S'))

while True:
    action = input()

    if action == 'collect the nets':
        if collected_fishes >= 20:
            print('Success! You managed to reach the quota!')
        else:
            print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected_fishes} "
                  f"tons of fish more.")
        if collected_fishes > 0:
            print(f'Amount of fish caught: {collected_fishes} tons.')
        [print(''.join(fishing_area[n])) for n in range(len(fishing_area))]
        break

    new_coord = (ship_coord[0] + movements[action][0], ship_coord[1] + movements[action][1])
    fishing_area[ship_coord[0]][ship_coord[1]] = '-'
    row, col = new_coord

    if 0 > row:
        row = fishing_area_size - 1
    elif row == fishing_area_size:
        row = 0

    if 0 > col:
        col = fishing_area_size - 1
    elif col == fishing_area_size:
        col = 0

    ship_coord = (row, col)
    curr_char = fishing_area[row][col]

    if curr_char == '-':
        fishing_area[row][col] = 'S'
    elif curr_char == 'W':
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the '
              f'ship: [{row},{col}]')
        break

    else:
        collected_fishes += int(curr_char)
        fishing_area[row][col] = 'S'