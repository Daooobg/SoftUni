rows = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for i in range(rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][rows - 1 - i])


print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")