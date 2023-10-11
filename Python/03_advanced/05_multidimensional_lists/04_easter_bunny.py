def is_valid_cell(row, col, size):
    return 0 <= row < size and 0 <= col < size


def collect_eggs(data, direction, bunny_position, size):
    total_eggs = 0
    eggs_positions = []
    if direction == 'down':
        for row in range(bunny_position[0] + 1, size):
            if data[row][bunny_position[1]] == 'X':
                break
            else:
                egg = int(data[row][bunny_position[1]])
                total_eggs += egg
                # if egg >= 1:
                eggs_positions.append([row, bunny_position[1]])

    elif direction == 'up':
        for row in range(bunny_position[0] - 1, - 1, - 1):
            if data[row][bunny_position[1]] == 'X':
                break
            else:
                egg = int(data[row][bunny_position[1]])
                total_eggs += egg
#                 if egg >= 1:
                eggs_positions.append([row, bunny_position[1]])

    elif direction == 'left':
        for col in range(bunny_position[1] - 1, - 1, - 1):
            if data[bunny_position[0]][col] == 'X':
                break
            else:
                egg = int(data[bunny_position[0]][col])
                total_eggs += egg
#                 if egg >= 1:
                eggs_positions.append([bunny_position[0], col])

    elif direction == 'right':
        for col in range(bunny_position[1] + 1, size):
            if data[bunny_position[0]][col] == 'X':
                break
            else:
                egg = int(data[bunny_position[0]][col])
                total_eggs += egg
#                 if egg >= 1:
                eggs_positions.append([bunny_position[0], col])

    return total_eggs, eggs_positions


matrix_size = int(input())
bunny_position = ()
matrix = []
max_eggs = 0
direction_coordinates = []
direction = ''

for row in range(matrix_size):
    current_row = input().split()
    if 'B' in current_row:
        bunny_position = (row, current_row.index('B'))
    matrix.append(current_row)

for current_direction in ['up', 'down', 'left', 'right']:
    result = collect_eggs(matrix, current_direction, bunny_position, matrix_size)
    if max_eggs < result[0]:
        max_eggs = result[0]
        direction_coordinates = result[1]
        direction = current_direction

print(direction)
print(*direction_coordinates, sep='\n')
print(max_eggs)