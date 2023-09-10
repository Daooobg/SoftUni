name_of_town = input()
type_of_package = input()
is_vip = input()
days = int(input())

total_price = 0
is_error = False

if days > 7:
    days -= 1

if days > 0:
    if name_of_town == 'Bansko' or name_of_town == 'Borovets':

        if type_of_package == 'withEquipment':
            total_price = days * 100
            if is_vip == 'yes':
                total_price -= total_price * 0.1
        elif type_of_package == 'noEquipment':
            total_price = days * 80
            if is_vip == 'yes':
                total_price -= total_price * 0.05
        else:
            print('"Invalid input!')

    elif name_of_town == 'Varna' or name_of_town == 'Burgas':

        if type_of_package == 'withBreakfast':
            total_price = days * 130
            if is_vip == 'yes':
                total_price -= total_price * 0.12
        elif type_of_package == 'noBreakfast':
            total_price = days * 100
            if is_vip == 'yes':
                total_price -= total_price * 0.7
        else:
            print('Invalid input!')
            is_error = True
    else:
        print('Invalid input!')
        is_error = True

else:
    print('Days must be positive number!')
    is_error = True

if not is_error:
    print(f'The price is {total_price:.2f}lv! Have a nice time!')