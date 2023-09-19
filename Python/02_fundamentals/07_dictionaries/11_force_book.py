command = input()

force_book = {}
force_users = []

while command != 'Lumpawaroo':
    if '|' in command:
        side, name = command.split(' | ')

        if name in force_users:
            command = input()
            continue
        else:
            force_users.append(name)

        if side in force_book.keys():
            force_book[side].append(name)
        else:
            force_book[side] = [name]

    elif '->' in command:
        name, side = command.split(' -> ')

        if name in force_users:
            for k, i in force_book.items():
                if name in i:
                    i.remove(name)
                    if side in force_book.keys():
                        force_book[side].append(name)
                    else:
                        force_book[side] = [name]

                    print(f"{name} joins the {side} side!")
                    break

        else:
            force_users.append(name)
            if side in force_book.keys():
                force_book[side].append(name)
            else:
                force_book[side] = [name]

            print(f'{name} joins the {side} side!')

    command = input()

for k, i in force_book.items():
    if len(i) > 0:
        print(f"Side: {k}, Members: {len(i)}")
        for name in i:
            print(f'! {name}')
