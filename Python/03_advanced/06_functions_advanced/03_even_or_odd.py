def even_odd(*args):
    action = args[-1]
    numbers = args[0:-1]

    if action == 'even':
        return [num for num in numbers if num % 2 == 0]
    elif action == 'odd':
        return [num for num in numbers if num % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))