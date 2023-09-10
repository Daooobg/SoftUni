sold_games = int(input())

hearthstone_sold = 0
fornite_sold = 0
overwatch_sold = 0
others_sold = 0

for _ in range(sold_games):
    current_game = input()

    if current_game == 'Hearthstone':
        hearthstone_sold += 1
    elif current_game == 'Fornite':
        fornite_sold += 1
    elif current_game == 'Overwatch':
        overwatch_sold += 1
    else:
        others_sold += 1


print(f'Hearthstone - {(hearthstone_sold / sold_games * 100):.2f}%')
print(f'Fornite - {(fornite_sold / sold_games * 100):.2f}%')
print(f'Overwatch - {(overwatch_sold / sold_games * 100):.2f}%')
print(f'Others - {(others_sold / sold_games * 100):.2f}%')