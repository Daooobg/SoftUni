def even_numbers(num_string: str):
    return list(filter(lambda n: n % 2 == 0, [int(n) for n in num_string.split()]))


numbers = input()
print(even_numbers(numbers))