from math import  floor

hours = int(input())
minutes = int(input())
add_minutes = 15

time_after_fifteen_minutes = hours * 60 + minutes + add_minutes

updated_hours = floor(time_after_fifteen_minutes / 60)
updated_minutes = time_after_fifteen_minutes % 60

if updated_hours >= 24:
    updated_hours = updated_hours % 24

if updated_minutes < 10:
    print(f'{updated_hours}:0{updated_minutes}')
else:
    print(f'{updated_hours}:{updated_minutes}')