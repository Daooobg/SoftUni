change = float(input())

change = int(change * 100)
number_of_coins = 0

while change != 0:
    if change >= 200:
        current_change = change // 200
        change -= current_change * 200
        number_of_coins += current_change
    elif change >= 100:
        change -= 100
        number_of_coins += 1
    elif change >= 50:
        change -= 50
        number_of_coins += 1
    elif change >= 20:
        current_change = change // 20
        change -= current_change * 20
        number_of_coins += current_change
    elif change >= 10:
        change -= 10
        number_of_coins += 1
    elif change >= 5:
        change -= 5
        number_of_coins += 1
    elif change >= 2:
        current_change = change // 2
        change -= current_change * 2
        number_of_coins += current_change
    elif change >= 1:
        change -= 1
        number_of_coins += 1

print(int(number_of_coins))