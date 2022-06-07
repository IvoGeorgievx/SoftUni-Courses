command = input()
to_do_notes = ["" for i in range(11)]

while command != 'End':
    current_command = command.split("-")
    priority = int(current_command[0])
    task = current_command[1]
    to_do_notes[priority] = task
    command = input()

final_list = [task for task in to_do_notes if task != ""]
print(final_list)