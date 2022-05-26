# Write a program that receives a single string (integers separated by a comma and space ", "),
# finds all the zeros, and moves them to the back without messing up the other elements.
# Print the resulting integer list.

string_nums = input().split(", ")
copy_list = list(map(int, string_nums))
not_zeros = []
zeros = []

for i in copy_list:
    if i == 0:
        zeros.append(i)
    else:
        not_zeros.append(i)
complete_list = not_zeros + zeros
print(complete_list)


