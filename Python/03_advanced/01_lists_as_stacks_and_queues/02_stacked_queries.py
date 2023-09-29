input_lines = int(input())

numbers_stack = []

commands_dic = {
    1: lambda x: numbers_stack.append(x[1]),
    2: lambda x: numbers_stack.pop() if numbers_stack else None,
    3: lambda x: print(max(numbers_stack)) if numbers_stack else None,
    4: lambda x: print(min(numbers_stack)) if numbers_stack else None
}

for _ in range(input_lines):
    command = [int(x) for x in input().split()]
    commands_dic[command[0]](command)


numbers_stack.reverse()
print(*numbers_stack, sep=', ')