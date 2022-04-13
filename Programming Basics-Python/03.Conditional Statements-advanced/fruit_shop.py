fruit_type = input()
day_of_the_week = input()
quantity = float(input())
fruit = 0
price = 0
day_of_the_week_is_valid = True
fruit_type_is_valid = True

if day_of_the_week == 'Monday' or day_of_the_week == 'Tuesday' \
    or day_of_the_week == 'Wednesday' or day_of_the_week == 'Thursday'\
    or day_of_the_week == 'Friday':
    day_of_the_week_is_valid = True
    if fruit_type == 'banana':
        price = 2.50
    elif fruit_type == 'apple':
        price = 1.20
    elif fruit_type == 'orange':
        price = 0.85
    elif fruit_type == 'grapefruit':
        price = 1.45
    elif fruit_type == 'kiwi':
        price = 2.70
    elif fruit_type == 'pineapple':
        price = 5.50
    elif fruit_type == 'grapes':
        price = 3.85
    else:
        fruit_type_is_valid = False




if day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
    day_of_the_week_is_valid = True
    if fruit_type == 'banana':
        price = 2.70
    elif fruit_type == 'apple':
        price = 1.25
    elif fruit_type == 'orange':
        price = 0.90
    elif fruit_type == 'grapefruit':
        price = 1.60
    elif fruit_type == 'kiwi':
        price = 3.00
    elif fruit_type == 'pineapple':
        price = 5.60
    elif fruit_type == 'grapes':
        price = 4.20

else:
    day_of_the_week_is_valid = False




















