key = int(input())
number_of_chars = int(input())

for _ in range(number_of_chars):
    current_char = input()
    print(chr(ord(current_char) + key), end='')