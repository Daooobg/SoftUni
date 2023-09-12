factor = int(input())
count = int(input())

result = []

for num in range(1, count + 1):
    result.append(abs(factor * num))

print(result)