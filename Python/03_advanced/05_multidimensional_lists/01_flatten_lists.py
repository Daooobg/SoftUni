input_line = input().split('|')

reversed_list = ' '.join(reversed(input_line))

result = reversed_list.split()

print(*result, sep=' ')