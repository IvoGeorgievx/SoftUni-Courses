def ticket_calculator(day):
    if day == "Monday":
        return 12
    elif day == 'Tuesday':
        return 12
    elif day == 'Wednesday':
        return 14
    elif day == 'Thursday':
        return 14
    elif day == 'Friday':
        return 12
    elif day == 'Saturday':
        return 16
    elif day == 'Sunday':
        return 16


day_of_the_week = input()
print(ticket_calculator(day_of_the_week))