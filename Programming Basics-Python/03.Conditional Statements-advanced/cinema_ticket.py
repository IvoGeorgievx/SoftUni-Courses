day_of_the_week = input()
mon_tues_fri = 12
wedn_thurst = 14
sat_sun = 16
ticket_price = 0

if day_of_the_week == 'Monday':
    ticket_price = mon_tues_fri
elif day_of_the_week == 'Tuesday':
    ticket_price = mon_tues_fri
elif day_of_the_week == 'Wednesday':
    ticket_price = wedn_thurst
elif day_of_the_week == 'Thursday':
    ticket_price = wedn_thurst
elif day_of_the_week == 'Friday':
    ticket_price = mon_tues_fri
elif day_of_the_week == 'Saturday':
    ticket_price = sat_sun
elif day_of_the_week == 'Sunday':
    ticket_price = sat_sun
print(ticket_price)


