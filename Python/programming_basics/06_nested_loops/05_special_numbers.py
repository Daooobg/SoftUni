input_number = int(input())

is_special = True

for f in range (1, 10):
    if input_number % f != 0:
        is_special = False

    for s in range(1, 10):
        if not is_special:
            is_special = True
            break
        if input_number % s != 0:
            is_special = False
        for t in range(1, 10):
            if not is_special:
                is_special = True
                break
            if input_number % t != 0:
                is_special = False
            for fourth in range(1, 10):
                if not is_special:
                    is_special = True
                    break
                if input_number % fourth != 0:
                    is_special = False
                if is_special:
                    print(f'{f}{s}{t}{fourth}', end=' ')

                is_special = True




