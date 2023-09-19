items = {}
legendary_item = ''

input_items = input().lower().split()
while True:




    for i in range(0, len(input_items), 2):

        if input_items[i + 1] in items.keys():
            items[input_items[i+1]] += int(input_items[i])
        else:
            items[input_items[i + 1]] = int(input_items[i])

        if items.get('shards'):
            if items['shards'] >= 250:
                items['shards'] -= 250
                legendary_item = 'Shadowmourne'
                break
        if items.get('fragments'):
            if items['fragments'] >= 250:
                items['fragments'] -= 250
                legendary_item = 'Valanyr'
                break
        if items.get('motes'):
            if items['motes'] >= 250:
                items['motes'] -= 250
                legendary_item = 'Dragonwrath'
                break

    if legendary_item:
        break

    input_items = input().lower().split()

print(f'{legendary_item} obtained!')

if items.get('shards'):
    print(f"shards: {items['shards']}")
else:
    print('shards: 0')

if items.get('fragments'):
    print(f"fragments: {items['fragments']}")
else:
    print('fragments: 0')

if items.get('motes'):
    print(f"motes: {items['motes']}")
else:
    print('motes: 0')

for k, i in items.items():
    if k != 'shards' and k != 'fragments' and k != 'motes':
        print(f'{k}: {i}')