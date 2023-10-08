from collections import deque

rows, columns = map(int, input().split())

matrix = [input().split() for _ in range(rows)]

command = input()

while command != 'END':
    action, *coordinates = command.split()

    if action == 'swap' and len(coordinates) == 4:
        coordinates = deque(map(int, coordinates))
        first_row_coord = coordinates.popleft()
        first_col_coord = coordinates.popleft()
        second_row_coord = coordinates.popleft()
        second_col_coord = coordinates.popleft()

        if (first_col_coord >= columns or first_row_coord >= rows or second_col_coord >= columns
                or second_row_coord >= rows):
            print('Invalid input!')

        else:
            matrix[first_row_coord][first_col_coord], matrix[second_row_coord][second_col_coord] = (
                matrix[second_row_coord][second_col_coord], matrix[first_row_coord][first_col_coord])

            for row in range(len(matrix)):
                print(' '.join(matrix[row]))

    else:
        print('Invalid input!')

    command = input()