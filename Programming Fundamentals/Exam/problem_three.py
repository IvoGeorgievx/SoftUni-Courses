phone_list = input().split(", ")
command = input()

while command != "End":
    exploded = command.split(" - ")
    command_type = exploded[0]
    new_phone = exploded[1]

    if command_type == 'Add':
        if new_phone not in phone_list:
            phone_list.append(new_phone)

    elif command_type == 'Remove':
        if new_phone in phone_list:
            phone_list.remove(new_phone)

    elif command_type == "Bonus phone":
        exploded_phone = new_phone.split(":")
        old_phone = exploded_phone[0]
        bnew_phone = exploded_phone[1]
        if old_phone in phone_list:
            x = phone_list.index(old_phone)
            phone_list.insert(x + 1, bnew_phone)

    elif command_type == "Last":
        if new_phone in phone_list:
            phone_list.remove(new_phone)
            phone_list.append(new_phone)

    command = input()

print(', '.join(phone_list))



