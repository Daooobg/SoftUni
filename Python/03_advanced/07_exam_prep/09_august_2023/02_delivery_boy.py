def is_valid_position(position, rows, cols):
    return 0 <= position[0] < rows and 0 <= position[1] < cols

rows, columns = list(map(int,input().split()))

matrix = []

is_get_out_from_the_field = False
ready_for_delivery = False
delivery_steps = 10

movements_dict = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    current_row = [char for char in input()]
    matrix.append(current_row)

    if 'B' in current_row:
        start_point = (row, current_row.index('B'))

delivery_boy_position = start_point

while True:
    if is_get_out_from_the_field:
        break
    action = input()
    new_position = (delivery_boy_position[0] + movements_dict[action][0], delivery_boy_position[1]
                    + movements_dict[action][1])

    if is_valid_position(new_position, rows, columns):
        r, c = new_position

        curr_char = matrix[r][c]

        if curr_char == 'P':
            matrix[r][c] = 'R'
            print('Pizza is collected. 10 minutes for delivery.')
            ready_for_delivery = True
        elif curr_char == 'A' and ready_for_delivery:
            matrix[r][c] = 'P'
            print('Pizza is delivered on time! Next order...')
            break
        elif curr_char == '-':
            matrix[r][c] = '.'
        elif curr_char == '*':
            continue

        delivery_boy_position = new_position


    else:
        is_get_out_from_the_field = True

if is_get_out_from_the_field:
    matrix[start_point[0]][start_point[1]] = ' '
    print('The delivery is late. Order is canceled.')
[print(''.join(matrix[n])) for n in range(len(matrix))]