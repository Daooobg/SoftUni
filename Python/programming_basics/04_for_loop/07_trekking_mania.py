number_of_groups = int(input())

musalla = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

number_of_climbers = 0

for _ in range(number_of_groups):
    current_group = int(input())
    number_of_climbers += current_group

    if current_group <= 5:
        musalla += current_group
    elif current_group <= 12:
        mont_blanc += current_group
    elif current_group <= 25:
        kilimanjaro += current_group
    elif current_group <= 40:
        k2 += current_group
    else:
        everest += current_group

for i in [musalla, mont_blanc, kilimanjaro, k2, everest]:
    print(f'{(i / number_of_climbers * 100):.2f}%')