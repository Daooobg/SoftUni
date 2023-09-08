budget = float(input())
amount_of_video_cards = int(input())
amount_of_processors = int(input())
amount_of_ram = int(input())

price_for_video_card = 250
total_price_for_video_cards = amount_of_video_cards * price_for_video_card

total_price_for_processors = (total_price_for_video_cards * 0.35) * amount_of_processors

total_price_for_ram = (total_price_for_video_cards * 0.1) * amount_of_ram

total_price = total_price_for_ram + total_price_for_processors + total_price_for_video_cards

if amount_of_video_cards > amount_of_processors:
    total_price -= total_price * 0.15

if budget >= total_price:
    print(f'You have {(budget - total_price):.2f} leva left!')
else:
    print(f'Not enough money! You need {(total_price - budget):.2f} leva more!')