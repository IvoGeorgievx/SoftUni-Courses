num_one = int(input())
num_two = int(input())
new_list = []

for num in range(1, num_two + 1):
    new_list.append(num * num_one)
print(new_list)

