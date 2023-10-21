import re

matrix = []
for _ in range(6):
    matrix.append(input().split())

input_coord = input()
numbers = re.findall(f'\d+', input_coord)
row, col = [int(num) for num in numbers]

movements = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    input_line = input().split(', ')
    action = input_line[0]
    if action == 'Stop':
        [print(' '.join(matrix[n])) for n in range(6)]
        break
    else:
        direction = input_line[1]
        new_position = (row + movements[direction][0], col + movements[direction][1])
        if 0 <= new_position[0] < 6 and 0 <= new_position[1] < 6:
            row, col = new_position
            if action == 'Create':
                if matrix[row][col] == '.':
                    matrix[row][col] = input_line[2]

            elif action == 'Update':
                if matrix[row][col] != '.':
                    matrix[row][col] = input_line[2]

            elif action == 'Delete':
                if matrix[row][col] != '.':
                    matrix[row][col] = '.'

            elif action == 'Read':
                if matrix[row][col] != '.':
                    print(matrix[row][col])
