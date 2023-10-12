def is_valid_position(cord):
    return 0 <= cord[0] < 5 and 0 <= cord[1] < 5


shooting_dict = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

movement_dict = {
    'up': lambda steps: (-steps, 0),
    'down': lambda steps: (steps, 0),
    'left': lambda steps: (0, -steps),
    'right': lambda steps: (0, steps)
}

matrix = []
current_position = ()
all_targets = 0

targets_coordinates = []

for row in range(5):
    current_row = input().split()

    if 'A' in current_row:
        current_position = (row, current_row.index('A'))

    if 'x' in current_row:
        all_targets += current_row.count('x')

    matrix.append(current_row)

for _ in range(int(input())):
    action, position, *args = input().split()
    if args:
        args = int(args[0])

    if action == 'move':
        movement_coord = movement_dict[position](args)

        new_position = (current_position[0] + movement_coord[0], current_position[1]
                        + movement_coord[1])
        if is_valid_position(new_position):
            if matrix[new_position[0]][new_position[1]] == '.':
                matrix[current_position[0]][current_position[1]] = '.'
                matrix[new_position[0]][new_position[1]] = 'A'
                current_position = new_position

    elif action == 'shoot':
        shooting_position = current_position
        while True:
            new_shooting_position = (shooting_position[0] + shooting_dict[position][0], shooting_position[1] +
                                     shooting_dict[position][1])

            if not is_valid_position(new_shooting_position):
                break

            current_target = matrix[new_shooting_position[0]][new_shooting_position[1]]
            matrix[new_shooting_position[0]][new_shooting_position[1]] = '.'

            if current_target == 'x':
                targets_coordinates.append([new_shooting_position[0], new_shooting_position[1]])
                break

            length = len(targets_coordinates)
            shooting_position = new_shooting_position

        if all_targets == len(targets_coordinates):
            break

if all_targets == len(targets_coordinates):
    print(f'Training completed! All {len(targets_coordinates)} targets hit.')
else:
    print(f'Training not completed! {all_targets - len(targets_coordinates)} targets left.')

[print(targets_coordinates[n]) for n in range(len(targets_coordinates))]