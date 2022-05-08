required_money = float(input())
money_owned = float(input())

spend_days = 0
days = 0

while True:
    command = input()
    money = float(input())
    days += 1
    if command == 'spend':
        spend_days += 1
        money_owned -= money
        if money_owned < 0:
            money_owned = 0

        if spend_days == 5:
            print(f"You can't save the money.")
            print(f'{days}')
            break
    else:
        money_owned += money
        spend_days = 0

    if money_owned >= required_money:
        print(f'You saved the money for {days} days.')
        break
