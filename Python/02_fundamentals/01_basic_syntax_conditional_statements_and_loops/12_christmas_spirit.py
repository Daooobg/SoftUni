quantity = int(input())
days_left = int(input())

total_costs = 0
total_spirit = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_costs += quantity * 2
        total_spirit += 5
    if day % 3 == 0:
        total_costs += quantity * 8
        total_spirit += 13
    if day % 5 == 0:
        total_costs += quantity * 15
        total_spirit += 17
    if day % 5 == 0 and day % 3 == 0:
        total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_costs += 23
        if day == days_left:
            total_spirit -= 30

print(f'Total cost: {total_costs}')
print(f'Total spirit: {total_spirit}')