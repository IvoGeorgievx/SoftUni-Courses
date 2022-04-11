# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст) -
# въведени от потребителя и проверява дали офисът на фирма е отворен,
# като работното време на офисът е от 10-18 часа, от понеделник до събота включително

hour = int(input())
day_of_the_week = input()
state = 'open'

if day_of_the_week == 'Monday' and 10 <= hour <= 18:
    print(state)
elif day_of_the_week == 'Tuesday' and 10 <= hour <= 18:
    print(state)
elif day_of_the_week == 'Wednesday' and 10 <= hour <= 18:
    print(state)
elif day_of_the_week == 'Thursday' and 10 <= hour <= 18:
    print(state)
elif day_of_the_week == 'Friday' and 10 <= hour <= 18:
    print(state)
elif day_of_the_week == 'Saturday' and 10 <= hour <= 18:
    print(state)
else:
    print('closed')





