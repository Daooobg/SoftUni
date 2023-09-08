budget = float(input())
background_actors = int(input())
single_price_for_clothing = float(input())

decor = budget * 0.1
total_price_for_clothing = single_price_for_clothing * background_actors

if background_actors > 150:
    total_price_for_clothing = total_price_for_clothing - (total_price_for_clothing * 0.1)

total_price_for_movie = decor + total_price_for_clothing

if budget >= total_price_for_movie:
    print('Action!')
    print(f'Wingard starts filming with {(budget - total_price_for_movie):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {(total_price_for_movie - budget):.2f} leva more.')