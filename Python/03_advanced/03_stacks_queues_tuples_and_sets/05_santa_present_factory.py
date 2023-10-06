from collections import deque

boxes_with_materials = deque(map(int, input().split()))
magic_values = deque(map(int, input().split()))

craft_toys = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}

while boxes_with_materials and magic_values:
    current_material = boxes_with_materials.pop()
    current_magic_level = magic_values.popleft()

    if current_material == 0 and current_magic_level == 0:
        continue
    elif current_material == 0:
        magic_values.appendleft(current_magic_level)
        continue
    elif current_magic_level == 0:
        boxes_with_materials.append(current_material)
        continue

    magic = current_magic_level * current_material

    if magic < 0:
        boxes_with_materials.append(abs(current_material + current_magic_level))
    elif magic == 150:
        craft_toys['Doll'] += 1
    elif magic == 250:
        craft_toys['Wooden train'] += 1
    elif magic == 300:
        craft_toys['Teddy bear'] += 1
    elif magic == 400:
        craft_toys['Bicycle'] += 1
    else:
        boxes_with_materials.append(current_material + 15)

craft_toys = {toy: quantity for toy, quantity in craft_toys.items() if quantity > 0}
sorted_toys = sorted(craft_toys)
if 'Doll' in sorted_toys and 'Wooden train' in sorted_toys:
    print("The presents are crafted! Merry Christmas!")
elif 'Teddy bear' in sorted_toys and 'Bicycle' in sorted_toys:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes_with_materials:
    # print(f"Materials left: {', '.join(list(reversed(list(map(str, boxes_with_materials)))))}")
    print(f"Materials left: {', '.join([str(item) for item in reversed(boxes_with_materials)])}")
if magic_values:
    print(f"Magic left: {', '.join(map(str, magic_values))}")

for item in sorted_toys:
    print(f'{item}: {craft_toys[item]}')