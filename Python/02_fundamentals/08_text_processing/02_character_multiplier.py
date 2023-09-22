first_string, second_string = input().split()

char_codes_sum = 0

min_length = min(len(first_string), len(second_string))

for i in range(min_length):
    char_codes_sum += ord(first_string[i]) * ord(second_string[i])

if len(first_string) > min_length:
    for char in first_string[min_length:]:
        char_codes_sum += ord(char)
elif len(second_string) > min_length:
    for char in second_string[min_length:]:
        char_codes_sum += ord(char)

print(char_codes_sum)