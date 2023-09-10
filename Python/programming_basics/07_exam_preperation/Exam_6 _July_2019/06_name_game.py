command_line = input()

winner_name = ''
winner_points = 0

while command_line != 'Stop':
    player_points = 0
    for l in range(len(command_line)):
        current_points = int(input())

        if ord(command_line[l]) == current_points:
            player_points += 10
        else:
            player_points += 2

    if winner_points <= player_points:
        winner_name = command_line
        winner_points = player_points

    command_line = input()

print(f'The winner is {winner_name} with {winner_points} points!')