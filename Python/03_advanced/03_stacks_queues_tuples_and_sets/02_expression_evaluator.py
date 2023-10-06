from collections import deque
from functools import reduce

expression = deque(input().split())
operators = ('*', '+', '-', '/')
numbers = deque()

action = {
    '*': lambda x: reduce(lambda a, b: a * b, x),
    '/': lambda x: reduce(lambda a, b: a / b, x),
    '+': lambda x: sum(x),
    '-': lambda x: reduce(lambda a, b: a - b, x)
}

while len(expression) > 0:
    operation = expression.popleft()

    if operation in operators:
        result = action[operation](numbers)
        numbers.clear()
        numbers.append(int(result))
    else:
        numbers.append(int(operation))

print(numbers[0])