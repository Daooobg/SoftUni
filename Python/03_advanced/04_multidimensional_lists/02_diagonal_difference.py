rows = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for i in range(rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][rows - 1 - i])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))