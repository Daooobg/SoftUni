numbers_list = input().split(', ')
current_group = 10
while True:
    if len(numbers_list) == 0:
        break
    current_group_numbers = [int(n) for n  in numbers_list if int(n) <= current_group]
    numbers_list = [n for n  in numbers_list if int(n) > current_group]
    print(f'Group of {current_group}\'s: {current_group_numbers}')
    current_group += 10