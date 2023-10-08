rows, columns = map(int, input().split())
matrix = []

for row in range(rows):
    current_row = []
    for column in range(columns):
        curr_word = chr(row + 97) + chr(row + column + 97) + chr(row + 97)
        current_row.append(curr_word)

    matrix.append(current_row)

for row in range(len(matrix)):
    print(' '.join(matrix[row]))