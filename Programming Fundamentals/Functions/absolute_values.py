nums = input().split(" ")
new_list = []

for i in nums:
    current_num = float(i)
    new_list.append(abs(current_num))
print(new_list)
