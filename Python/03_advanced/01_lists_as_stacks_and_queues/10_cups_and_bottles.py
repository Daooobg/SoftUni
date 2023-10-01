from collections import deque

cups = deque(int(x) for x in input().split())
bottles = deque(int(x) for x in input().split())

waste = 0

while True:
    if not bottles or not cups:
        break
    bottle = bottles.pop()

    cups[0] -= bottle

    if cups[0] <= 0:
        waste += abs(cups[0])
        cups.popleft()

if bottles:
    print('Bottles:', end=' ')
    print(*bottles, sep=' ')
if cups:
    print('Cups:', end=' ')
    print(*cups, sep=' ')
print(f'Wasted litters of water: {waste}')