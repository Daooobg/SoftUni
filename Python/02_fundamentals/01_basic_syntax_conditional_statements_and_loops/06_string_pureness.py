number_of_strings = int(input())

for _ in range(number_of_strings):
    string = input()
    is_pure = True
    for i in range(len(string)):
        ascii_code = ord(string[i])
        if ascii_code == 44 or ascii_code == 46 or ascii_code == 95:
            is_pure = False
            break

    if is_pure:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')