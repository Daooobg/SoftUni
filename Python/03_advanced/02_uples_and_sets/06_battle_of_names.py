n = int(input())

odd_set = set()
even_set = set()

for i in range(n):
    name = input()
    char_code_sum = 0
    for char in name:
        char_code_sum += ord(char)

    char_code_sum = int(char_code_sum / (i + 1))
    if char_code_sum % 2 == 0:
        even_set.add(char_code_sum)
    else:
        odd_set.add(char_code_sum)


odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    odd_set.union(even_set)
    print(f"{', '.join(map(str, odd_set))}")
elif odd_sum > even_sum:
    diff = odd_set.difference(even_set)
    print(f"{', '.join(map(str, sorted(odd_set, reverse=True)))}")
else:
    odd_set.update(even_set)
    print(f"{', '.join(map(str, odd_set))}")