input_numbers = list(map(int, input().split()))

average_number = sum(input_numbers ) / len(input_numbers)

sorted_numbers = sorted(input_numbers, reverse=True)
top_numbers = [num for num in sorted_numbers if num > average_number]
top_five_numbers = top_numbers[:5]

if top_five_numbers:
    print(' '.join(list(map(str, top_five_numbers))))
else:
    print('No')