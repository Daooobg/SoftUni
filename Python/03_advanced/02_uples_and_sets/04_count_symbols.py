text = input()

char_count = {}
for char in text:
    if char not in char_count:
        char_count[char] = 0
    char_count[char] += 1

sorted_chars = sorted(char_count)

for char in sorted_chars:
    print(f'{char}: {char_count[char]} time/s')