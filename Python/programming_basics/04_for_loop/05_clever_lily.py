lilys_age = int(input())
washing_machine_price = float(input())
price_for_one_toy = int(input())

saving_money = 0
toys = 0
gets_money = 0

for n in range(1, lilys_age + 1):

    if n % 2 == 0:
        gets_money += 10
        saving_money += gets_money - 1
    else:
        toys += 1

saving_money += toys * price_for_one_toy

if saving_money >= washing_machine_price:
    print(f'Yes! {(saving_money - washing_machine_price):.2f}')
else:
    print(f'No! {(washing_machine_price - saving_money):.2f}')