numbers_input = list(map(int, input().split()))

sum = 0

while len(numbers_input) != 0:
    index = int(input())
    if index < 0:
        removed_num = numbers_input[0]
        numbers_input[0] = numbers_input[-1]

    elif index >= len(numbers_input):
        removed_num = numbers_input[-1]
        numbers_input[-1] = numbers_input[0]
    else:
        removed_num = numbers_input[index]
        numbers_input.pop(index)

    sum += removed_num

    for i, num in enumerate(numbers_input):
        if num > removed_num:
            numbers_input[i] -= removed_num
        else:
            numbers_input[i] += removed_num

print(sum)