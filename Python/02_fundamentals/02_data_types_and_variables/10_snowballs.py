number_of_snowballs = int(input())

highest_snowball = 0
highest_snowball_weight = 0
highest_snowball_time = 0
highest_snowball_quality = 0

for _ in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    current_high = (snowball_weight / snowball_time) ** snowball_quality

    if highest_snowball <= current_high :
        highest_snowball = current_high
        highest_snowball_weight = snowball_weight
        highest_snowball_time = snowball_time
        highest_snowball_quality = snowball_quality

print(f'{highest_snowball_weight} : {highest_snowball_time} = {int(highest_snowball)} ({highest_snowball_quality})')