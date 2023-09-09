input_line = input()

prime_numbers_sum = 0
non_prime_numbers_sum = 0

while input_line != 'stop':
    counter = 0
    current_number = int(input_line)

    if current_number < 0:
        current_number = 0
        print('Number is negative.')

    for n in range(2, current_number + 1):
        if current_number % n == 0:
            counter += 1
            if counter > 2:
                break

    if counter > 1:
        non_prime_numbers_sum += current_number
    else:
        prime_numbers_sum += current_number

    input_line = input()

print(f'Sum of all prime numbers is: {prime_numbers_sum}')
print(f'Sum of all non prime numbers is: {non_prime_numbers_sum}')