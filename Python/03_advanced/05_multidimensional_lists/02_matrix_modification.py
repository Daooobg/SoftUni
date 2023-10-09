rows = int(input())

matrix = [list(map(int, input().split())) for _ in range(rows)]

while True:
    command = input()
    if command == 'END':
        break

    action, *rest = command.split()
    row, col, num = map(int, rest)

    if 0 <= row < rows and 0 <= col < rows:
        if action == 'Add':
            matrix[row][col] += num
        elif action == 'Subtract':
            matrix[row][col] -= num
    else:
        print('Invalid coordinates')

[print(*matrix[n], sep=' ') for n in range(len(matrix))]