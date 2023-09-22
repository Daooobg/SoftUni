input_line = input()

length = len(input_line)

result = ''
explosion_sum = 0

for i in range(length):
    if input_line[i] == '>':
        explosion_sum += int(input_line[i + 1])
        result += input_line[i]
    else:
        if explosion_sum > 0:
            explosion_sum -= 1
        else:
            result += input_line[i]

print(result)