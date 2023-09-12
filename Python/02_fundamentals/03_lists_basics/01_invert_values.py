numbers_string = input()

numbers_list = numbers_string.split(' ')
opposite_numbers = []

for number in numbers_list:
    opposite_numbers.append(-int(number))

print(opposite_numbers)