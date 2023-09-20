def shooting_gallery(targets, commands):
    targets = list(map(int, targets))

    for line in commands:
        if line == 'End':
            break

        command, *args = line.split()
        if command == 'Shoot':
            index, power = map(int, args)
            if 0 <= index < len(targets):
                targets[index] -= power
                if targets[index] <= 0:
                    targets.pop(index)
        elif command == 'Add':
            index, value = map(int, args)
            if 0 <= index < len(targets):
                targets.insert(index, value)
            else:
                print("Invalid placement!")
        elif command == 'Strike':
            index, radius = map(int, args)
            start = index - radius
            end = index + radius
            if 0 <= start < len(targets) and 0 <= end < len(targets):
                del targets[start:end+1]
            else:
                print("Strike missed!")

    return '|'.join(map(str, targets))


initial_targets = input().split()
commands = []
while True:
    command = input()
    if command == 'End':
        break
    commands.append(command)

result = shooting_gallery(initial_targets, commands)
print(result)
