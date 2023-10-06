from collections import deque

bees = deque(map(int, input().split()))
nectar_value = deque(map(int, input().split()))
operations = deque(input().split())

honey = 0

function = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: abs(a - b),
    '/': lambda a, b: a / b,
    '*': lambda a, b: a * b
}

while True:
    if not bees or not nectar_value or not operations:
        break

    bee = bees.popleft()
    nectar = nectar_value.pop()

    if bee > nectar:
        bees.appendleft(bee)
    elif bee < nectar:
        operation = operations.popleft()
        honey += function[operation](bee, nectar)

print(f'Total honey made: {honey}')
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar_value:
    print(f"Nectar left: {', '.join(map(str, nectar_value))}")