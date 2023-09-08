number_of_pen_packages = int(input())
number_of_tag_packages = int(input())
liters_of_blackboard_cleaner = int(input())
discount = int(input())

pen_price = 5.80
tag_price = 7.20
cleaner_price = 1.20

price_before_discount = (number_of_pen_packages * pen_price + number_of_tag_packages * tag_price +
                         liters_of_blackboard_cleaner * cleaner_price)

total_price = price_before_discount - (price_before_discount * (discount / 100))

print(total_price)