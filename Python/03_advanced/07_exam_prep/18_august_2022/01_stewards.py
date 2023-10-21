from collections import deque

seats = input().split(', ')
seat_numbers1 = deque(map(int, input().split(', ')))
seat_numbers2 = deque(map(int, input().split(', ')))

matches_seats = []
rotation = 0

while True:
    first_num = seat_numbers1.popleft()
    second_num = seat_numbers2.pop()
    rotation += 1

    char = chr(first_num + second_num)
    curr_seat1 = f'{first_num}{char}'
    curr_seat2 = f'{second_num}{char}'

    if curr_seat1 in seats or curr_seat2 in seats:
        if curr_seat1 in seats:
            matches_seats.append(curr_seat1)
            seats.remove(curr_seat1)
        elif curr_seat2 in seats:
            matches_seats.append(curr_seat2)
            seats.remove(curr_seat2)

        if len(matches_seats) == 3:
            break

    else:
        seat_numbers1.append(first_num)
        seat_numbers2.appendleft(second_num)

    if rotation == 10:
        break

print(f"Seat matches: {', '.join(matches_seats)}")
print(f"Rotations count: {rotation}")