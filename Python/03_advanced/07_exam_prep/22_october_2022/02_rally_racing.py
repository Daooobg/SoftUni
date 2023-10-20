n = int(input())
racing_car_num = input()
car_position = (0, 0)
distance = 0

actions_dict = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix = []
tunnels_position = []

for row in range(n):
    curr_row = input().split()
    matrix.append(curr_row)

    if 'T' in curr_row:
        start_index = 0
        for _ in range(curr_row.count('T')):
            char_position = curr_row.index('T', start_index)
            tunnels_position.append((row, char_position))
            start_index = char_position + 1

matrix[0][0] = 'C'

while True:
    action = input()
    if action == 'End':
        print(f'Racing car {racing_car_num} DNF.')
        break

    new_position = (car_position[0] + actions_dict[action][0], car_position[1] + actions_dict[action][1])
    r, c = new_position

    if 0 <= r < n and 0 <= c < n:
        curr_char = matrix[r][c]
        matrix[r][c] = 'C'
        matrix[car_position[0]][car_position[1]] = '.'
        distance += 10

        if curr_char == 'F':
            print(f'Racing car {racing_car_num} finished the stage!')
            break

        elif curr_char == 'T':
            matrix[r][c] = '.'
            if new_position == tunnels_position[0]:
                new_position = tunnels_position[1]
            else:
                new_position = tunnels_position[0]
            matrix[new_position[0]][new_position[1]] = '.'
            distance += 20

        car_position = new_position

print(f'Distance covered {distance} km.')
[print(''.join(matrix[n])) for n in range(len(matrix))]
