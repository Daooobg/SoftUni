n1 = int(input())
n2 = int(input())
operator = input()

sum = 0

if operator == '-' or operator == '+' or operator == '*':
    odd_or_even = 'odd'
    if operator == '+':
        sum = n1 + n2
    elif operator == '-':
        sum = n1 - n2
    else:
        sum = n1 * n2

    if sum % 2 == 0:
        odd_or_even = 'even'

    print(f'{n1} {operator} {n2} = {sum} - {odd_or_even}')

elif operator == '%' or operator == '/':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        if operator == '/':
            sum = n1 / n2
            print(f'{n1} {operator} {n2} = {sum:.2f}')

        else:
            sum = n1 % n2
            print(f'{n1} {operator} {n2} = {sum}')
