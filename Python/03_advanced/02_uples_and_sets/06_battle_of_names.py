n = int(input())

odd_set = set()
even_set = set()

for i in range(n):
    name = input()
    char_code_sum = 0
    for char in name:
        char_code_sum += ord(char)

    char_code_sum = char_code_sum // (i + 1)
    if char_code_sum % 2 == 0:
        even_set.add(char_code_sum)
    else:
        odd_set.add(char_code_sum)


odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    print(*odd_set.union(even_set), sep=', ')
elif odd_sum > even_sum:
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')