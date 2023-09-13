def sum_numbers(a: int, b: int):
    return a + b


def subtract(a: int, b: int):
    return a - b


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(subtract(sum_numbers(first_num, second_num), third_num))