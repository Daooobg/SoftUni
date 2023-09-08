cake_width = int(input())
cake_length = int(input())

total_pieces = cake_length * cake_width
taken_pieces = 0

while total_pieces > taken_pieces:
    current_pieces = input()

    if current_pieces == 'STOP':
        break

    taken_pieces += int(current_pieces)


if taken_pieces <= total_pieces:
    print(f'{total_pieces - taken_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {taken_pieces - total_pieces} pieces more.')