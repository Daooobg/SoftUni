required_amount_of_protection = int(input())
required_amount_of_paint = int(input())
required_amount_of_thinner = int(input())
hours_to_finish_the_job = int(input())

price_of_protection = 1.5
price_of_paint = 14.5
price_of_thinner = 5
price_of_bags = 0.4

total_price_of_protection = (required_amount_of_protection + 2 ) * price_of_protection
total_price_of_paint = (required_amount_of_paint * 1.1) * price_of_paint
total_price_of_thinner = required_amount_of_thinner * price_of_thinner

total_price_for_materials = total_price_of_protection + total_price_of_paint + total_price_of_thinner + price_of_bags
total_price_for_work = (total_price_for_materials * 0.3) * hours_to_finish_the_job

total_price = total_price_for_work + total_price_for_materials

print(total_price)