from sys import maxsize

def create_matrix(cols):
    return [list(map(int, input().split())) for _ in range(cols)]


def max_sum_of_matrix(matrix, cols, rows):
    max_sum = -maxsize
    start_col = 0
    start_row = 0

    for col in range(cols - 2):
        for row in range(rows - 2):
            current_sum = (matrix[col][row] + matrix[col][row + 1] + matrix[col][row + 2] + matrix[col + 1][row] +
                           matrix[col + 1][row + 1] + matrix[col + 1][row + 2] + matrix[col + 2][row] + matrix[col + 2][row + 1] + matrix[col + 2][row + 2])

            if current_sum > max_sum:
                max_sum = current_sum
                start_col = col
                start_row = row

    print(f'Sum = {max_sum}')

    for i in range(start_col, start_col + 3):
        current_row = matrix[i][start_row:start_row + 3]
        print(*current_row, sep=' ')

columns, rows = map(int, input().split())

max_sum_of_matrix(create_matrix(columns), columns, rows)