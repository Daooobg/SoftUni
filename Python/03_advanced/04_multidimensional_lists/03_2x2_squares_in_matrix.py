columns, rows = input().split()
columns = int(columns)
rows = int(rows)


def create_matrix():
    matrix = [input().split() for _ in range(columns)]
    return matrix


def find_square_matrix(matrix, cols, rows):
    number_of_square_matrices = 0
    for i in range(cols - 1):
        for j in range(rows - 1):
            if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
                number_of_square_matrices += 1

    return number_of_square_matrices


print(find_square_matrix(create_matrix(), columns, rows))