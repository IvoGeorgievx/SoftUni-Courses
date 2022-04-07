required_sleep_time = 30000
rest_days = int(input())

days_of_the_year = 365
working_days = days_of_the_year - rest_days
play_time = (working_days * 63) + (rest_days * 127)

if required_sleep_time >= play_time:
    plus_sleep_time = required_sleep_time - play_time
    plus_hours = plus_sleep_time // 60
    plus_minutes = plus_sleep_time % 60
    print('Tom sleeps well')
    print(f'{round(plus_hours)} hours and {round(plus_minutes)} minutes less for play')
elif required_sleep_time <= play_time:
    minus_sleep_time = play_time - required_sleep_time
    minus_hours = minus_sleep_time // 60
    minus_minutes = minus_sleep_time % 60
    print('Tom will run away')
    print(f'{round(minus_hours)} hours and {round(minus_minutes)} minutes more for play')






