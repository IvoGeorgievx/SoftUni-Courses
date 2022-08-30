matrix = []

row = int(input())

for _ in range(row):
    current_row = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(current_row)

print(matrix)