elements = input().split()

command = input()

movements = 0
number_of_turns = 0

while command != 'end':
    if len(elements) == 0:
        break
    number_of_turns += 1
    movements += 1
    first_index, second_index = list(map(int, command.split()))

    if first_index == second_index or first_index < 0 or second_index < 0 or first_index >= len(elements) or second_index >= len(elements):
        append_element = f"-{movements}a"

        elements.insert(int(len(elements) / 2), append_element)
        elements.insert(int(len(elements) / 2), append_element)

        print('Invalid input! Adding additional elements to the board')
        command = input()
        continue

    if elements[first_index] == elements[second_index]:
        found_element = elements[first_index]
        print(f'Congrats! You have found matching elements - {found_element}!')
        elements.remove(found_element)
        elements.remove(found_element)
    else:
        print('Try again!')

    command = input()

if elements:
    print('Sorry you lose :(')
    print(' '.join(elements))
else:
    print(f'You have won in {number_of_turns} turns!')



"""
1 1 2 2 3 3 4 4 5 5
1 0
-1 0
1 0 
1 0 
1 0 
end

"""