price_for_chicken_portion = 10.35
price_for_fish_portion = 12.40
price_for_vegetarian_portion = 8.15

amount_of_chicken_portions = int(input())
amount_of_fish_portions = int(input())
amount_of_vegetarian_portions = int(input())

total_price_for_all_portions = (amount_of_chicken_portions * price_for_chicken_portion + amount_of_fish_portions *
                                price_for_fish_portion + amount_of_vegetarian_portions * price_for_vegetarian_portion)

price_for_desserts = total_price_for_all_portions * 0.2

total_price = total_price_for_all_portions + price_for_desserts + 2.50

print(total_price)