screen_type = input()
rows = int(input())
columns = int(input())

income = 0

cinema_capacity = rows * columns

if screen_type == 'Premiere':
    income = cinema_capacity * 12
elif screen_type == 'Normal':
    income = cinema_capacity * 7.5
elif screen_type == 'Discount':
    income = cinema_capacity * 5

print(f'{income:.2f} leva')