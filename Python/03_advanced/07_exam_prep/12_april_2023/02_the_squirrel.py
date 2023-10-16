from collections import deque

field_size = int(input())
actions = deque(input().split(', '))

squirrel_position = ()
field = []
collected_hazelnuts = 0
is_out_from_field = False

movements = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(field_size):
    current_row = [char for char in input()]
    field.append(current_row)

    if 's' in current_row:
        squirrel_position = (row, current_row.index('s'))

while collected_hazelnuts < 3:
    if not actions:
        print('There are more hazelnuts to collect.')
        break

    current_action = actions.popleft()
    new_position = (squirrel_position[0] + movements[current_action][0], squirrel_position[1] +
                    movements[current_action][1])
    r, c = new_position

    if 0 <= r < field_size and 0 <= c < field_size:
        current_char = field[r][c]
        field[r][c] = 's'
        field[squirrel_position[0]][squirrel_position[1]] = '*'
        squirrel_position = new_position
        if current_char == 'h':
            collected_hazelnuts += 1
        elif current_char == 't':
            print('Unfortunately, the squirrel stepped on a trap...')
            break
    else:
        print('The squirrel is out of the field.')
        break

if collected_hazelnuts == 3:
    print('Good job! You have collected all hazelnuts!')
print(f'Hazelnuts collected: {collected_hazelnuts}')