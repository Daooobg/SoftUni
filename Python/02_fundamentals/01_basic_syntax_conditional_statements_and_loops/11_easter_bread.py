budget = float(input())
price_for_flour = float(input())

colored_eggs = 0
total_bread = 0
prev_budget = 0

price_for_eggs = price_for_flour * 0.75
price_for_one_litter_milk = price_for_flour * 1.25 / 4

# budget -= price_for_flour + price_for_eggs + price_for_one_litter_milk

while True:
    prev_budget = budget
    budget -= price_for_flour +  price_for_eggs + price_for_one_litter_milk

    if budget >= 0:
        total_bread += 1

        if total_bread % 3 == 0:
            colored_eggs += 3
            colored_eggs -= total_bread - 2
        else:
            colored_eggs += 3

    else:
        break

print(f'You made {total_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {prev_budget:.2f}BGN left.')