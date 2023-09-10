name_of_the_team = input()
number_of_games = int(input())

total_points = 0
won_gamse = 0
draw_games = 0
lost_games = 0

if number_of_games == 0:
    print(f'{name_of_the_team} hasn\'t played any games during this season.')

else:
    for _ in range(number_of_games):
        current_game = input()

        if current_game == 'W':
            won_gamse += 1
            total_points += 3
        elif current_game == 'D':
            draw_games += 1
            total_points += 1
        elif current_game == 'L':
            lost_games += 1

    print(f'{name_of_the_team} has won {total_points} points during this season.')
    print('Total stats:')
    print(f'## W: {won_gamse}')
    print(f'## D: {draw_games}')
    print(f'## L: {lost_games}')
    print(f'Win rate: {(won_gamse / number_of_games * 100):.2f}%')