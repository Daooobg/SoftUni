def min_max_sum(string: str):
    numbers_in_list = [int(n) for n in string.split()]

    print(f'The minimum number is {min(numbers_in_list)}')
    print(f'The maximum number is {max(numbers_in_list)}')
    print(f'The sum number is: {sum(numbers_in_list)}')


input_line = input()
min_max_sum(input_line)