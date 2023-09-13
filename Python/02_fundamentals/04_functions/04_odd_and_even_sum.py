def sum_of_odd_and_even(num: int):
    number_as_string = str(num)

    odd_num = [int(n) for n in number_as_string if int(n) % 2 != 0]
    even_num = [int(n) for n in number_as_string if int(n) % 2 == 0]

    return f'Odd sum = {sum(odd_num)}, Even sum = {sum(even_num)}'


number = int(input())

print(sum_of_odd_and_even(number))
