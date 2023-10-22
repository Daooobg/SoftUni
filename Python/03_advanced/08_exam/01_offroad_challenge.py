from collections import deque

fuels = deque(map(int, input().split()))
consumptions = deque(map(int, input().split()))
fuels_needed = deque(map(int, input().split()))

altitude = 0
altitude_list = []
isFail = False

for _ in range(4):
    curr_fuel = fuels.pop()
    curr_consumption = consumptions.popleft()
    curr_fuel_needed = fuels_needed.popleft()
    altitude += 1

    if (curr_fuel - curr_consumption) >= curr_fuel_needed:
        altitude_list.append(f'Altitude {altitude}')
    else:
        isFail = True
        break

if altitude_list:
    for curr_altitude in altitude_list:
        print(f'John has reached: {curr_altitude}')

if isFail:
    if altitude_list:
        print(f'John did not reach: Altitude {altitude}')
        print('John failed to reach the top.')
        print(f"Reached altitudes: {', '.join(altitude_list)}")
    else:
        print(f'John did not reach: Altitude {altitude}')
        print("John failed to reach the top.\nJohn didn't reach any altitude.")
else:
    print('John has reached all the altitudes and managed to reach the top!')
