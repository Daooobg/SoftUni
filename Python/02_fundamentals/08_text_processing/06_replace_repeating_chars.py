string = input()

previous_char = ''

for char in string:
    if char != previous_char:
        print(char, end='')
        previous_char = char