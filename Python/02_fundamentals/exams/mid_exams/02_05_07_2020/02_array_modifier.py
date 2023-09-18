numbers_list = input().split()

command = input().split()

while command[0] != 'end':
    action = command[0]
    if action == 'swap':
        first_index = int(command[1])
        second_index = int(command[2])

        numbers_list[first_index], numbers_list[second_index] = numbers_list[second_index], numbers_list[first_index]
    elif action == 'multiply':
        first_index = int(command[1])
        second_index = int(command[2])

        numbers_list[first_index] = str(int(numbers_list[first_index]) * int(numbers_list[second_index]))

    elif action == 'decrease':
        numbers_list = [str(int(num) - 1) for num in numbers_list]

    command = input().split()

print(', '.join(numbers_list))