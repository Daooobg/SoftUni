number_of_fillings = int(input())

current_capacity = 0

for _ in range(number_of_fillings):
    current_water = int(input())
    if current_capacity + current_water <= 255:
        current_capacity += current_water
    else:
        print('Insufficient capacity!')

print(current_capacity)