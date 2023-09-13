def perfect_number(num: int):
    divisors_list = [divisor for divisor in range(1, num) if num % divisor == 0]

    if sum(divisors_list) == num:
        return 'We have a perfect number!'
    else:
        return 'It\'s not so perfect.'


number = int(input())
print(perfect_number(number))