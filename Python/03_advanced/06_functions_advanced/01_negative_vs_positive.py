def sub_positive_negative_num(*args):
    positive_sum = 0
    negative_sum = 0

    for num_as_str in args:
        number = int(num_as_str)
        if number > 0:
            positive_sum += number
        else:
            negative_sum += number

    return negative_sum, positive_sum


result = sub_positive_negative_num(*input().split())

negative_sum, positive_sum = result
print(negative_sum)
print(positive_sum)
if positive_sum + negative_sum > 0:
    print('The positives are stronger than the negatives')
elif positive_sum + negative_sum < 0:
    print('The negatives are stronger than the positives')

