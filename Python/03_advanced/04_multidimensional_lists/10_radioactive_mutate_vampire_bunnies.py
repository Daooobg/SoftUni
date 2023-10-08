def is_valid_cell(row, col, row_size, col_size):
    return 0 <= row < row_size and 0 <= col < col_size

rows, cols = map(int, input().split())

movements = {
    'U': lambda cr: (cr[0] - 1, cr[1]),
    'D': lambda cr: (cr[0] + 1, cr[1]),
    'L': lambda cr: (cr[0], cr[1] - 1),
    'R': lambda cr: (cr[0], cr[1] + 1),
}

matrix = []
player_start_coord = ()
is_won = True
is_out = False

for r in range(rows):
    current_row = input()
    if 'P' in current_row:
        player_start_coord = (r, current_row.index('P'))
    matrix.append([char for char in current_row])

actions = [char for char in input()]

for action in actions:
    current_player_coord = movements[action](player_start_coord)

    matrix[player_start_coord[0]][player_start_coord[1]] = '.'

    if not is_valid_cell(current_player_coord[0], current_player_coord[1], rows, cols):
        is_out = True
    else:
        matrix[current_player_coord[0]][current_player_coord[1]] = 'P'
        player_start_coord = current_player_coord

    bunnies_position = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'B':
                bunnies_position.append((row, col))

    for bonnie_coord in bunnies_position:
        for bonnie_movement in movements:
            new_row, new_col = movements[bonnie_movement](bonnie_coord)
            if is_valid_cell(new_row, new_col, rows, cols):
                if matrix[new_row][new_col] == 'P':
                    is_won = False
                matrix[new_row][new_col] = 'B'

    if not is_won or is_out:
        break

[print(''.join(matrix[n])) for n in range(rows)]
if is_won:
    print(f'won: {player_start_coord[0]} {player_start_coord[1]}')
else:
    print(f'dead: {player_start_coord[0]} {player_start_coord[1]}')