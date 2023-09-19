n = int(input())

parking = {}

for _ in range(n):
    command = input().split()

    action = command[0]

    if action == 'register':
        name = command[1]
        plate = command[2]

        if name in parking.keys():
            print(f"ERROR: already registered with plate number {parking[name]}")
        else:
            parking[name] = plate
            print(f"{name} registered {plate} successfully")

    elif action == 'unregister':
        name = command[1]
        if name in parking.keys():
            parking.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")


for k, i in parking.items():
    print(f"{k} => {i}")