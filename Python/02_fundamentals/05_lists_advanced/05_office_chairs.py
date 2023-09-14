number_of_rooms = int(input())

free_chairs = 0
is_free = True

for current_room in range(1, number_of_rooms + 1):
    information = input().split()
    current_chairs = len(information[0])
    current_visitors = int(information[1])

    if current_chairs > current_visitors:
        free_chairs += current_chairs - current_visitors
    elif current_chairs < current_visitors:
        print(f'{current_visitors - current_chairs} more chairs needed in room {current_room}')
        is_free = False

if is_free:
    print(f'Game On, {free_chairs} free chairs left')