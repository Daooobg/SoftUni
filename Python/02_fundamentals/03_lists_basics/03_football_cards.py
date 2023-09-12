input_line = input()
send_off_players = input_line.split(' ')

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
is_stop_the_game = False

for send_off_player in send_off_players:
    split_send_off_player = send_off_player.split('-')
    team = split_send_off_player[0]
    player_number = int(split_send_off_player[1])

    if team == 'A' and player_number in team_a:
        team_a.remove(int(split_send_off_player[1]))
    elif team == 'B' and player_number in team_b:
        team_b.remove(int(split_send_off_player[1]))

    if len(team_a) < 7 or len(team_b) < 7:
        is_stop_the_game = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if is_stop_the_game:
    print('Game was terminated')