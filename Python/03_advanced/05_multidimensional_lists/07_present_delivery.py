def is_valid_position(cord, size):
    return 0 <= cord[0] < size and 0 <= cord[1] < size


number_of_presents = int(input())
neighborhood_size = int(input())

matrix = []
santa_coord = ()
total_number_of_nice_kids = 0

movement_dict = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(neighborhood_size):
    current_row = input().split()

    if 'S' in current_row:
        santa_coord = (row, current_row.index('S'))
    if 'V' in current_row:
        total_number_of_nice_kids += current_row.count('V')

    matrix.append(current_row)

number_of_nice_kids = total_number_of_nice_kids

while True:
    action = input()

    if action == 'Christmas morning':
        break

    current_coord = (santa_coord[0] + movement_dict[action][0], santa_coord[1] + movement_dict[action][1])

    if is_valid_position(current_coord, neighborhood_size):
        r, c = current_coord

        current_char = matrix[r][c]
        matrix[santa_coord[0]][santa_coord[1]] = '-'
        matrix[r][c] = 'S'

        santa_coord = (r, c)

        if current_char == 'V':
            number_of_nice_kids -= 1
            number_of_presents -= 1
        elif current_char == 'C':
            start_row = r - 1 if r >= 0 else 0
            end_row = r + 1 if r < neighborhood_size else neighborhood_size - 1
            start_col = c - 1 if c >= 0 else 0
            end_col = c + 1 if c < neighborhood_size else neighborhood_size - 1

            for current_row in range(start_row, end_row + 1):
                for current_col in range(start_col, end_col + 1):
                    char = matrix[current_row][current_col]
                    if char == '-' or char == 'S':
                        continue

                    matrix[current_row][current_col] = '-'
                    if char == 'X':
                        number_of_presents -= 1
                    elif char == 'V':
                        number_of_presents -= 1
                        number_of_nice_kids -= 1

                    if number_of_presents == 0:
                        break

        if number_of_presents == 0:
            break

if number_of_nice_kids > 0 and number_of_presents == 0:
    print('Santa ran out of presents!')

[print(' '.join(matrix[n])) for n in range(len(matrix))]

if number_of_nice_kids == 0:
    print(f'Good job, Santa! {total_number_of_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {number_of_nice_kids} nice kid/s.')