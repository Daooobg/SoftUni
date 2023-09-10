budget = float(input())
number_nights = int(input())
price_per_night = float(input())
percentage_additional_costs = int(input())

if number_nights > 7:
    price_per_night -= price_per_night * 0.05

cost_for_hotel = number_nights * price_per_night
additional_costs = budget * percentage_additional_costs / 100
total_costs = cost_for_hotel + additional_costs

if total_costs <= budget:
    print(f'Ivanovi will be left with {(budget - total_costs):.2f} leva after vacation.')
else:
    print(f'{(total_costs - budget):.2f} leva needed.')
