rows, cols = map(int, input().split(','))

matrix = []
total_cheese = 0
mouse_position = ()

mouse_movements = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    current_row = [char for char in input()]

    if 'C' in current_row:
        total_cheese += current_row.count('C')
    if 'M' in current_row:
        mouse_position = (row, current_row.index('M'))

    matrix.append(current_row)

while True:
    action = input()
    if action == 'danger':
        print('Mouse will come back later!')
        break

    new_position = (mouse_position[0] + mouse_movements[action][0], mouse_position[1] + mouse_movements[action][1])
    r, c = new_position
    if 0 <= r < rows and 0 <= c < cols:
        current_char = matrix[r][c]
        if current_char == '@':
            continue

        matrix[mouse_position[0]][mouse_position[1]] = '*'
        matrix[r][c] = 'M'
        mouse_position = new_position

        if current_char == 'C':
            total_cheese -= 1
            if total_cheese == 0:
                print('Happy mouse! All the cheese is eaten, good night!')
                break
        elif current_char == 'T':
            print('Mouse is trapped!')
            break

    else:
        print('No more cheese for tonight!')
        break


[print(''.join(matrix[n])) for n in range(len(matrix))]