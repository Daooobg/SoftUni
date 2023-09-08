length = int(input())
width = int(input())
height = int(input())
percent_occupied = int(input())

fish_tank_volume = (length * width * height) / 1000

required_water = fish_tank_volume * (1 - (percent_occupied / 100))

print(required_water)