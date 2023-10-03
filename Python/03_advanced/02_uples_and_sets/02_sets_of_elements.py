first_set_length, second_set_length = (map(int, input().split()))

first_set = {input() for _ in range(first_set_length)}
second_set = {input() for _ in range(second_set_length)}

intersection_set = first_set.intersection(second_set)
print('\n'.join(intersection_set))