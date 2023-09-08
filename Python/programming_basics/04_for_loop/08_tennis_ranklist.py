from math import floor

number_of_tournaments = int(input())
starting_points = int(input())

won_tournaments = 0
won_points = 0

for _ in range(number_of_tournaments):
    stage = input()

    if stage == 'W':
        won_points += 2000
        won_tournaments += 1
    elif stage == 'F':
        won_points += 1200
    elif stage == 'SF':
        won_points += 720

print(f'Final points: {won_points + starting_points}')
print(f'Average points: {floor(won_points / number_of_tournaments)}')
print(f'{(won_tournaments / number_of_tournaments * 100):.2f}%')
