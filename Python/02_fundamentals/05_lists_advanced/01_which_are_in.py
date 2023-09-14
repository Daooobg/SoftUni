first_str = input().split(', ')
second_str = input()

result = []

for string in first_str:
    if string in second_str:
        result.append(string)

print(result)