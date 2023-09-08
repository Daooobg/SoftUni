numbers = int(input())

max_number = 0
sum_numbers = 0

for i in range(0, numbers):
    current_number = int(input())

    if i == 0:
        max_number = current_number

    if current_number > max_number:
        max_number = current_number

    sum_numbers += current_number

if max_number == sum_numbers - max_number:
    print('Yes')
    print(f'Sum = {max_number}')

else:
    diff = abs(max_number - (sum_numbers - max_number))
    print('No')
    print(f'Diff = {diff}')



# other solution

# from sys import  maxsize
#
# n = int(input())
# max_number = -maxsize
# sum_numbers = 0
#
# for i in range(0, n):
#     num = int(input())
#
#     if num > max_number:
#         max_number = num
#
#     sum_numbers += num
#
# if max_number == sum_numbers - max_number:
#     print('Yes')
#     print(f'Sum = {max_number}')
#
# else:
#     print('No')
#     sum_numbers = sum_numbers - max_number
#     print(f'Diff = {abs(max_number - sum_numbers)}')