def is_valid_position(cord, size):
    return 0 <= cord[0] < size and 0 <= cord[1] < size

rows = int(input())

movement_dict = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix = []
alice_position = ()
collected_tea_bags = 0

for row in range(rows):
    row_input = input().split()
    if 'A' in row_input:
        alice_position = (row, row_input.index('A'))
    matrix.append(row_input)


while True:
    action = input()

#     clear 'A' from field and replace it with '*'
    matrix[alice_position[0]][alice_position[1]] = '*'

    new_position = (alice_position[0] + movement_dict[action][0], alice_position[1] + movement_dict[action][1])

    if is_valid_position(new_position, rows):
        alice_position = new_position

        # read the current sigh
        current_mark = matrix[alice_position[0]][alice_position[1]]
        # replace the sigh with *
        matrix[alice_position[0]][alice_position[1]] = '*'

        if current_mark == 'R':
            break
        elif current_mark.isdigit():
            collected_tea_bags += int(current_mark)

        if collected_tea_bags >= 10:
            break

    else:
        break

if collected_tea_bags >= 10:
    print('She did it! She went to the party.')
else:
    print('Alice didn\'t make it to the tea party.')

[print(' '.join(matrix[n])) for n in range(len(matrix))]