n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

all_bobs_coord = input().split()


def is_valid_cell(row, col, size):
    return 0 <= row < size and 0 <= col < size


for bomb_coord in all_bobs_coord:
    bomb_row, bomb_col = list(map(int, bomb_coord.split(',')))

    if is_valid_cell(bomb_row, bomb_col, n):
        bomb_power = matrix[bomb_row][bomb_col]
        if bomb_power <= 0:
            continue
    else:
        continue

    for row_offset in [-1, 0, 1]:
        for col_offset in [-1, 0, 1]:
            new_row, new_col = bomb_row - row_offset, bomb_col - col_offset
            if is_valid_cell(new_row, new_col, n):
                if matrix[new_row][new_col] > 0:
                    matrix[new_row][new_col] -= bomb_power

alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]

print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum(alive_cells)}')
[print(*matrix[i], sep=' ') for i in range(n)]