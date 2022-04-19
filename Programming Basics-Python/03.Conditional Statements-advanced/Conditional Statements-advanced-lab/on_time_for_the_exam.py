exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute
diff = exam_time - arrival_time

if diff < 0:
    print('Late')
    diff = abs(diff)
    if diff >= 60:
        hours = diff // 60
        minutes = diff % 60
        print(f'{hours}:{minutes:02d} hours after the start')
    else:
        print(f'{diff} minutes after the start')
elif 0 <= diff <= 30:
    print('On time')
    if diff > 0:
        print(f'{diff} minutes before the start')
elif diff > 30:
    print('Early')
    if diff >= 60:
        hours = diff // 60
        minutes = diff % 60
        print(f'{hours}:{minutes:02d} hours before the start')
    else:
        print(f'{diff} minutes before the start')





