numbers_list = [int(num) for num in input().split(' ')]
removed_numbers_count = int(input())

sort_numbers = sorted(numbers_list)[removed_numbers_count:]

result_list =[]

for index in range(len(numbers_list)):
    if numbers_list[index] in sort_numbers:
        result_list.append(str(numbers_list[index]))


print(', '.join(result_list))