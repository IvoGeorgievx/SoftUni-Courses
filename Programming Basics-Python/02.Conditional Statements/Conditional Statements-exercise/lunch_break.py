from math import ceil

series_name = str(input())
series_duration = int(input())
break_duration = int(input())

lunch_break = break_duration * (1 / 8)
rest_break = break_duration * 0.25
time_left = break_duration - (lunch_break + rest_break)

if time_left >= series_duration:
    print(f'You have enough time to watch {series_name}'
          f' and left with {ceil(time_left - series_duration)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, "
          f"you need {ceil(series_duration - time_left)} more minutes.")



