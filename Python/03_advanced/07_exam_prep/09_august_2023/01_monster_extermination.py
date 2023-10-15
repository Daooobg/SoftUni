from collections import deque

monsters_armor = deque(map(int, input().split(',')))
soldier_strikes = deque(map(int, input().split(',')))

total_killed_monsters = 0

while True:
    if not monsters_armor:
        break
    if not soldier_strikes:
        break
    current_monster = monsters_armor.popleft()

    current_strike = soldier_strikes.pop()

    if current_strike > current_monster:
        if soldier_strikes:
            soldier_strikes[-1] += current_strike - current_monster
        else:
            soldier_strikes.append(current_strike - current_monster)
        total_killed_monsters += 1
    elif current_monster > current_strike:
        monsters_armor.append(current_monster - current_strike)
    else:
        total_killed_monsters += 1


if not monsters_armor:
    print('All monsters have been killed!')

if not soldier_strikes:
    print('The soldier has been defeated.')

print(f'Total monsters killed: {total_killed_monsters}')