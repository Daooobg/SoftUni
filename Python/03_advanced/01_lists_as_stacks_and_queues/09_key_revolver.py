from collections import deque

bullet_price = int(input())
size_of_gun_barrel = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
intelligence_value = int(input())

current_shoot = 0

while bullets:
    if not locks:
        break

    current_shoot += 1
    current_bullet = bullets.pop()
    current_lock = locks[0]

    if current_lock >= current_bullet:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')

    if current_shoot % size_of_gun_barrel == 0 and len(bullets) > 0:
        print('Reloading!')

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_miney = intelligence_value - (current_shoot * bullet_price)
    print(f'{len(bullets)} bullets left. Earned ${earned_miney}')