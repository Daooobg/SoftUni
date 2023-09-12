fires = input().split('#')
water_capacity = int(input())

effort = 0
total_fire = 0
cells = []

for fire in fires:
    fire = fire.split(' = ')
    fire_type = fire[0]
    fire_level = int(fire[1])

    if (fire_level >= 1) and (fire_level <= 50):
        if fire_type != 'Low':
            continue
    elif fire_level <= 80:
        if fire_type != 'Medium':
            continue
    elif fire_level <= 125:
        if fire_type != 'High':
            continue
    else:
        continue

    if water_capacity < fire_level:
        continue

    water_capacity -= fire_level
    effort += fire_level * 0.25
    total_fire += fire_level
    cells.append(fire_level)

print('Cells:')
for cell in cells:
    print(f' - {cell}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
