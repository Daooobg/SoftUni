def letters_change_numbers(string):
    number = int(string[1: -1])
    result = 0

    if string[0].isupper():
        divider = ord(string[0]) - 64
        result = number / divider
    else:
        multiplier = ord(string[0]) - 96
        result = number * multiplier

    if string[-1].isupper():
        subtractor = ord(string[-1]) - 64
        result -= subtractor
    else:
        add = ord(string[-1]) - 96
        result += add

    return result


result = 0
for string in input().split():
    result += letters_change_numbers(string)

print(f'{result:.2f}')