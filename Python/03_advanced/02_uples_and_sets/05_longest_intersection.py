n = int(input())

longest_intersection = set()

for _ in range(n):
    set_a_range, set_b_range = input().split('-')

    set_a_start_range, set_a_end_range = set_a_range.split(',')
    set_b_start_range, set_b_end_range = set_b_range.split(',')

    set_a = {x for x in range(int(set_a_start_range), int(set_a_end_range) + 1)}
    set_b = {x for x in range(int(set_b_start_range), int(set_b_end_range) + 1)}

    set_intersection = set_a.intersection(set_b)

    if len(set_intersection) > len(longest_intersection):
        longest_intersection = set_intersection

print(f"Longest intersection is [{', '.join(map(str, longest_intersection))}] with length {len(longest_intersection)}")