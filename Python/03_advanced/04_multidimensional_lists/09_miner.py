def is_valid_cell(row, col, size):
    return 0 <= row < size and 0 <= col < size


actions_dict = {
    'up': lambda cr, size: (cr[0] - 1, cr[1]) if is_valid_cell(cr[0] - 1, cr[1], size) else (cr[0], cr[1]),
    'down': lambda cr, size: (cr[0] + 1, cr[1]) if is_valid_cell(cr[0] + 1, cr[1], size) else (cr[0], cr[1]),
    'left': lambda cr, size: (cr[0], cr[1] - 1) if is_valid_cell(cr[0], cr[1] - 1, size) else (cr[0], cr[1]),
    'right': lambda cr, size: (cr[0], cr[1] + 1) if is_valid_cell(cr[0], cr[1] + 1, size) else (cr[0], cr[1])
}

size = int(input())
actions = input().split()

matrix = []
start_coord = ()
number_of_coals = 0
is_over = False

for i in range(size):
    matrix_row = input().split(' ')
    if 's' in matrix_row:
        start_coord = (i ,matrix_row.index('s'))

    number_of_coals += matrix_row.count('c')

    matrix.append(matrix_row)

for action in actions:
    start_coord = actions_dict[action](start_coord, size)
    if matrix[start_coord[0]][start_coord[1]] == 'c':
        number_of_coals -= 1
        matrix[start_coord[0]][start_coord[1]] = '*'
    elif matrix[start_coord[0]][start_coord[1]] == 'e':
        is_over = True
        break

if is_over:
    print(f'Game over! ({start_coord[0]}, {start_coord[1]})')
else:
    if number_of_coals > 0:
        print(f'{number_of_coals} pieces of coal left. ({start_coord[0]}, {start_coord[1]})')
    else:
        print(f'You collected all coal! ({start_coord[0]}, {start_coord[1]})')