price_of_puzzle = 2.60
price_of_doll = 3
price_of_teddy_bear = 4.10
price_of_minion = 8.20
price_of_truck = 2

price_of_tour = float(input())
amount_of_puzzles = int(input())
amount_of_doll = int(input())
amount_of_teddy_bear = int(input())
amount_of_minion = int(input())
amount_of_truck = int(input())

amount_of_toys = amount_of_puzzles + amount_of_minion + amount_of_truck + amount_of_doll + amount_of_teddy_bear

total_price = (price_of_puzzle * amount_of_puzzles + price_of_doll * amount_of_doll + price_of_teddy_bear *
               amount_of_teddy_bear + amount_of_minion * price_of_minion + price_of_truck * amount_of_truck)

if amount_of_toys >= 50:
    total_price = total_price - (total_price * 0.25)

rent = total_price * 0.1

profit = total_price - rent

if profit >= price_of_tour:
    print(f'Yes! {(profit - price_of_tour):.2f} lv left.')
else:
    print(f'Not enough money! {(price_of_tour - profit):.2f} lv needed.')
