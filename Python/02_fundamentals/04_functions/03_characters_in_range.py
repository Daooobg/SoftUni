def chars_range(char_one: str, char_two: str):
    char_one_code = ord(char_one)
    char_two_code = ord(char_two)

    char_range = [chr(char) for char in range(char_one_code + 1, char_two_code)]

    return ' '.join(char_range)


first_char = input()
second_char = input()
print(chars_range(first_char, second_char))