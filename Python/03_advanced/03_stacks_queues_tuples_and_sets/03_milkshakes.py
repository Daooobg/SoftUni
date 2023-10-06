from collections import deque

chocolates = deque(map(int, input().split(', ')))
cups_of_milk = deque(map(int, input().split(', ')))

milkshakes = 0

while milkshakes < 5:
    if len(chocolates) == 0 or len(cups_of_milk) == 0:
        break

    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    elif chocolates[-1] <= 0:
        chocolates.pop()
        continue

    elif cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    if cups_of_milk[0] == chocolates[-1]:
        milkshakes += 1
        cups_of_milk.popleft()
        chocolates.pop()
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates[-1] -=5

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

print(f"Chocolate: {'empty' if len(chocolates) == 0 else ', '.join(map(str, chocolates))}")
print(f"Milk: {'empty' if len(cups_of_milk) == 0 else ', '.join(map(str, cups_of_milk))}")