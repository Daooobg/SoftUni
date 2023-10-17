rows, cols = map(int, input().split())

playground = []
blind_man_position = ()
touched_players = 0
total_movements = 0

movement_positions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    current_row = input().split(' ')
    playground.append(current_row)

    if 'B' in current_row:
        blind_man_position = (row, current_row.index('B'))

while touched_players < 3:
    action = input()
    if action == 'Finish':
        break

    new_position = (blind_man_position[0] + movement_positions[action][0], blind_man_position[1]
                    + movement_positions[action][1])

    r, c = new_position

    if 0 <= r < rows and 0 <= c < cols:
        current_char = playground[r][c]
        if current_char == 'O':
            continue

        playground[blind_man_position[0]][blind_man_position[1]] = '-'
        playground[r][c] = 'B'
        total_movements += 1
        blind_man_position = new_position

        if current_char == 'P':
            touched_players += 1


print('Game over!')
print(f'Touched opponents: {touched_players} Moves made: {total_movements}')