def is_valid_cell(row, col, size):
    return 0 <= row < size and 0 <= col < size


board_size = int(input())
board = [[char for char in input()] for _ in range(board_size)]

knights_movements = {
    'TL': lambda position: (position[0] -2, position[1] - 1),
    'TR': lambda position: (position[0] -2, position[1] + 1),
    'UL': lambda position: (position[0] -1, position[1] - 2),
    'UR': lambda position: (position[0] -1, position[1] + 2),
    'DL': lambda position: (position[0] + 1, position[1] - 2),
    'DR': lambda position: (position[0] + 1, position[1] + 2),
    'BL': lambda position: (position[0] + 2, position[1] - 1),
    'BR': lambda position: (position[0] + 2, position[1] + 1),
}

knights_on_board = []
total_knights = 0


for row in range(board_size):
    for col in range(board_size):
        if board[row][col] == 'K':
            knights_on_board.append((row, col))
            total_knights += 1

total_removed = 0

while True:
    max_destroyed_knights = 0
    destroyed_knights_positions = ()

    for knight_position in knights_on_board:
        current_destroyed_knights = 0
        for movement in knights_movements:
            coord = knights_movements[movement](knight_position)
            if is_valid_cell(coord[0], coord[1], board_size):
                coord = knights_movements[movement](knight_position)
                if board[coord[0]][coord[1]] == 'K':
                    current_destroyed_knights += 1

        if current_destroyed_knights > max_destroyed_knights:
            max_destroyed_knights = current_destroyed_knights
            destroyed_knights_positions = knight_position

    if max_destroyed_knights == 0:
        break
    else:
        total_removed += 1
        knights_on_board.remove(destroyed_knights_positions)
        board[destroyed_knights_positions[0]][destroyed_knights_positions[1]] = '0'

print(total_removed)