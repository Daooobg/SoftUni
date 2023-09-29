from collections import deque

clothes = deque([int(x) for x in input().split()])
rack_capacity = int(input())

rack_quantity = 1
current_rack_capacity = rack_capacity

while clothes:
    current_clothes_quantity = clothes.pop()
    if current_rack_capacity - current_clothes_quantity >= 0:
        current_rack_capacity -= current_clothes_quantity
    else:
        rack_quantity += 1
        current_rack_capacity = rack_capacity - current_clothes_quantity

print(rack_quantity)
