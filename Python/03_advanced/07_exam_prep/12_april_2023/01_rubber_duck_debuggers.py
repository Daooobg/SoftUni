from collections import deque

times_for_tasks = deque(map(int, input().split()))
number_of_tasks = deque(map(int, input().split()))

tasks_dict = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while times_for_tasks and number_of_tasks:
    current_time_for_task = times_for_tasks.popleft()
    current_number_of_task = number_of_tasks.pop()

    current_time = current_time_for_task * current_number_of_task

    if current_time <= 60:
        tasks_dict['Darth Vader Ducky'] += 1
    elif current_time <= 120:
        tasks_dict['Thor Ducky'] += 1
    elif current_time <= 180:
        tasks_dict['Big Blue Rubber Ducky'] += 1
    elif current_time <= 240:
        tasks_dict['Small Yellow Rubber Ducky'] += 1
    else:
        times_for_tasks.append(current_time_for_task)
        number_of_tasks.append(current_number_of_task - 2)

print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
for k, v in tasks_dict.items():
    print(f'{k}: {v}')
