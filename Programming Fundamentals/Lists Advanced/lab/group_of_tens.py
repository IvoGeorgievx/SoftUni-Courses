def group_of_tens(info):
    max_value = max(info)
    boundary = 10
    for current_num in info:
        if current_num >= boundary:
            numbers.remove(current_num)
        boundary += 10




numbers = list(map(int, input().split(", ")))
print(group_of_tens(numbers))

