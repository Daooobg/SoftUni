size_of_field = int(input())

action_dict = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
destroyed_ships = 0

battlefield = []
submarine_position = ()
numbers_of_hits_from_mine = 0

for row in range(size_of_field):
    curr_row = [char for char in input()]
    battlefield.append(curr_row)

    if 'S' in curr_row:
        submarine_position = (row, curr_row.index('S'))

while True:
    action = input()

    new_position = (submarine_position[0] + action_dict[action][0], submarine_position[1] + action_dict[action][1])
    r, c = new_position

    if 0 <= r < size_of_field and 0 <= c < size_of_field:
        curr_char = battlefield[r][c]
        battlefield[submarine_position[0]][submarine_position[1]] = '-'
        battlefield[r][c] = 'S'
        submarine_position = new_position

        if curr_char == '*':
            numbers_of_hits_from_mine += 1
            if numbers_of_hits_from_mine == 3:
                print(f'Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!')
                break
        elif curr_char == 'C':
            destroyed_ships += 1
            if destroyed_ships == 3:
                print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
                break


[print(''.join(battlefield[n])) for n in range(len(battlefield))]