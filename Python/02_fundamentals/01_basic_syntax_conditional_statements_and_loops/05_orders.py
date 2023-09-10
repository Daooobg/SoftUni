number_of_orders = int(input())

total_price = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    number_of_capsules = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= number_of_capsules <= 2000:
        current_price = price_per_capsule * days * number_of_capsules
        print(f'The price for the coffee is: ${current_price:.2f}')
        total_price += current_price

print(f'Total: ${total_price:.2f}')