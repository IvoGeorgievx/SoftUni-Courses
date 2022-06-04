nums = input().split(", ")
nums = list(map(int, nums))
even_index_numbers = []

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        even_index_numbers.append(i)

print(even_index_numbers)