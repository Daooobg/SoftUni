budget = float(input())
season = input()

cost_for_holiday = 0
destination = ''
place = ''

if season == 'summer':
    place = 'Camp'
elif season == 'winter':
    place = 'Hotel'

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        cost_for_holiday = budget * 0.3
    elif season == 'winter':
        cost_for_holiday = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        cost_for_holiday = budget * 0.4
    elif season == 'winter':
        cost_for_holiday = budget * 0.8
else:
    destination = 'Europe'
    cost_for_holiday = budget * 0.9
    place = 'Hotel'



print(f'Somewhere in {destination}')
print(f'{place} - {cost_for_holiday:.2f}')