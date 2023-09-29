from collections import deque

quantity_of_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    if quantity_of_food - order >= 0:
        orders.popleft()
        quantity_of_food -= order
    else:
        print(f"Orders left: {' '.join([str(o) for o in orders])}")
        break

else:
    print('Orders complete')