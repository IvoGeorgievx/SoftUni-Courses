def rounding(i):
    new_list = []
    for k in i:
        current_num = round(float(k))
        new_list.append(round(current_num))
    return new_list


the_input = input().split(" ")
print(rounding(the_input))
