flat_width = int(input())
flat_length = int(input())
flat_height = int(input())

flat_capacity = flat_height * flat_length * flat_width
occupied_space = 0

while flat_capacity > occupied_space:
    input_line = input()

    if input_line == 'Done':
        break

    occupied_space += int(input_line)

if flat_capacity >= occupied_space:
    print(f'{flat_capacity - occupied_space} Cubic meters left.')
else:
    print(f'No more free space! You need {occupied_space - flat_capacity} Cubic meters more.')