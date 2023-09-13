"""
    Recursive
"""


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


first_number = int(input())
second_number = int(input())
print(f'{(factorial(first_number) / factorial(second_number)):.2f}')

# Other way

# def factorial(num: int):
#     factorial_number = num
#     for n in range(num - 1, 0, -1):
#         factorial_number = factorial_number * n
#
#     return factorial_number
#
#
# first_number = int(input())
# second_number = int(input())
# print(f'{(factorial(first_number) / factorial(second_number)):.2f}')