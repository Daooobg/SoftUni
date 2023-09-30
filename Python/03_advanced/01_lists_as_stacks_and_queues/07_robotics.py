from datetime import datetime, timedelta
from collections import deque

robots_data = {robot_data.split('-')[0]: [int(robot_data.split('-')[1]), 0] for robot_data in input().split(';')}
time = input()
start_time = datetime.strptime(time, '%H:%M:%S')

products = deque()
current_product = input()
while current_product != 'End':
    products.append(current_product)
    current_product = input()

while len(products) > 0:
    current_product = products.popleft()

    start_time += timedelta(seconds=1)
    robots_data = {robot: [times[0], times[1] - 1] if times[1] != 0 else times for robot, times in robots_data.items()}
    free_robots = list(filter(lambda x: x[1][1] == 0, robots_data.items()))

    if free_robots:
        robots_data[free_robots[0][0]][1] = free_robots[0][1][0]
        print(f"{free_robots[0][0]} - {current_product} [{start_time.strftime('%H:%M:%S')}]")
    else:
        products.append(current_product)