from math import ceil

wall_height = int(input())
wall_width = int(input())
not_be_painted_percentage = int(input())

line_input = input()
to_be_painted = (wall_width * wall_height) * 4
to_be_painted -= ceil(to_be_painted * not_be_painted_percentage / 100)

while line_input != 'Tired!':
    current_painted = int(line_input)

    to_be_painted -= current_painted

    if to_be_painted <= 0:
        break

    line_input = input()

if to_be_painted < 0:
    print(f'All walls are painted and you have {abs(to_be_painted)} l paint left!')
elif to_be_painted == 0:
    print('All walls are painted! Great job, Pesho!')
else:
    print(f'{to_be_painted} quadratic m left.')