def loading_bar(percentage):
    if percentage == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        current_percent = (percentage // 10) * '%'
        dots = (10 - (percentage // 10)) * '.'

        print(f'{percentage}% [{current_percent}{dots}]')
        print('Still loading...')


loading_bar(percentage=int(input()))