resources = {}

while True:
    resource = input()

    if resource == 'stop':
        break

    quantity = int(input())

    if resource in resources.keys():
        resources[resource] += quantity
    else:
        resources[resource] = quantity

for k, v in resources.items():
    print(f'{k} -> {v}')