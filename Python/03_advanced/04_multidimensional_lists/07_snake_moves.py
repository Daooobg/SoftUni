from collections import deque

rows, columns = map(int, input().split())
snake_word = input()

current_word = deque(char for char in snake_word)

matrix = []

for row in range(rows):
    current_row = []
    for col in range(columns):
        if not current_word:
            current_word = deque(char for char in snake_word)

        current_char = current_word.popleft()

        current_row.append(current_char)

    if row % 2 == 0:
        matrix.append(current_row)
    else:
        matrix.append(reversed(current_row))


for row in range(len(matrix)):
    print(''.join(matrix[row]))