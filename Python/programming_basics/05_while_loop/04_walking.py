total_steps = 0

while total_steps < 10000:
    current_steps = input()

    if current_steps == 'Going home':
        current_steps = int(input())
        total_steps += current_steps
        break

    total_steps += int(current_steps)


if total_steps < 10000:
    print(f'{10000 - total_steps} more steps to reach goal.')
else:
    print('Goal reached! Good job!')
    print(f'{total_steps - 10000} steps over the goal!')