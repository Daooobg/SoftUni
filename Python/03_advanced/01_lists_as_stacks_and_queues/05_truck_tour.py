from collections import deque

number_of_pumps = int(input())


def get_information():
    pumps = deque()
    for _ in range(number_of_pumps):
        pumps.append([int(x) for x in input().split()])

    return pumps


pumps_info = get_information()

for i in range(number_of_pumps):
    petrol_capacity = 0
    for pump_info in pumps_info:
        current_petrol, distance = pump_info
        petrol_capacity += current_petrol - distance

        if petrol_capacity < 0:
            break

    if petrol_capacity >= 0:
        print(i)
        break

    pumps_info.append(pumps_info.popleft())