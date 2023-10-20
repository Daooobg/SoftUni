from collections import deque

milligrams_of_coffeine = list(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))

total_caffeine = 0

while True:
    if not milligrams_of_coffeine or not energy_drinks:
        break

    curr_coffe = milligrams_of_coffeine.pop()
    curr_energy_drink = energy_drinks.popleft()

    curr_caffeine = curr_coffe * curr_energy_drink

    if total_caffeine + curr_caffeine <= 300:
        total_caffeine += curr_caffeine
    else:
        energy_drinks.append(curr_energy_drink)
        if total_caffeine > 0:
            total_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print('At least Stamat wasn\'t exceeding the maximum caffeine.')

print(f'Stamat is going to sleep with {total_caffeine} mg caffeine.')