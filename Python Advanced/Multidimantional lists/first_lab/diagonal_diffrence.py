size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split(" ")])

primary_sum = []
secondary_sum = []

for idx in range(size):
    primary_sum.append(matrix[idx][idx])
    secondary_sum.append(matrix[idx][size - idx - 1])

print(abs(sum(primary_sum) - sum(secondary_sum)))