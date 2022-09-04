matrix = []

rows = int(input())

for _ in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    matrix.append(current_row)

complete_matrix = []

for i in matrix:
    complete_matrix.extend(i)

print(complete_matrix)