def accommodate_new_pets(capacity, max_allowed_weight, *args):
    hotel_dict = {}
    number_of_pets = 0
    is_hotel_full = False

    for arg in args:
        if number_of_pets == capacity:
            is_hotel_full = True
            break

        pet , weight = arg
        weight = float(weight)
        if weight > max_allowed_weight:
            continue
        number_of_pets += 1
        if pet not in hotel_dict.keys():
            hotel_dict[pet] = [weight]
        else:
            hotel_dict[pet].append(weight)

    result = ''

    if is_hotel_full:
        result += 'You did not manage to accommodate all pets!\n'
    else:
        result += f'All pets are accommodated! Available capacity: {capacity - number_of_pets}.\n'

    result += f'Accommodated pets:\n'
    result += '\n'.join(f'{kvp[0]}: {len(kvp[1])}' for kvp in sorted(hotel_dict.items()))

    return result


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
