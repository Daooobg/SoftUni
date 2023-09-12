numbers_list = [int(num) for num in input().split(', ')]
number_of_beggars = int(input())

beggars_sum = [0] * number_of_beggars

for index, num in enumerate(numbers_list):
    beggars_sum[index % number_of_beggars] += num

print(beggars_sum)