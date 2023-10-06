sequence_one = set(map(int, input().split()))
sequence_two = set(map(int, input().split()))

n = int(input())

for _ in range(n):
    action, place, *numbers = input().split()
    numbers =  set(map(int, numbers))

    if action == 'Add' :
        if place == 'First':
            sequence_one.update(numbers)
        elif place == 'Second':
            sequence_two.update(numbers)

    elif action == 'Remove':
        if place == 'First':
            sequence_one.difference_update(numbers)
        elif place == 'Second':
            sequence_two.difference_update(numbers)

    elif action == 'Check' and place == 'Subset':
        if sequence_one.issubset(sequence_two) or sequence_two.issubset(sequence_one):
            print('True')
        else:
            print('False')

print(f"{', '.join(map(str,sorted(sequence_one)))}")
print(f"{', '.join(map(str,sorted(sequence_two)))}")