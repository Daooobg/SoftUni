number_of_chars = int(input())

total_sum = 0

for _ in range(number_of_chars):
    current_char = input()
    total_sum += ord(current_char)

print(f'The sum equals: {total_sum}')