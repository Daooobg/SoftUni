targets = [int(t) for t in input().split()]

action = input()
shoot_targets = 0

while action != 'End':
    current_target = int(action)

    if  current_target >= 0 and current_target < len(targets):
        current_value = int(targets[current_target])
        if targets[current_target] != -1:
            shoot_targets += 1
            targets[current_target] = -1
        for index, target in enumerate(targets):
            if target != -1:
                if target > current_value:
                    targets[index] -= current_value
                else:
                    targets[index] += current_value
    action = input()

targets_as_string = ' '.join(map(str, targets))

print(f'Shot targets: {shoot_targets} -> {targets_as_string}')