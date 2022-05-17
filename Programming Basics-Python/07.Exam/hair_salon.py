target = int(input())
money_earned = 0
command = input()
target_achieved = False
while command != 'closed':
    haircut = command
    if haircut == 'haircut':
        gender = input()
        if gender == 'mens':
            money_earned += 15
        elif gender == 'ladies':
            money_earned += 20
        elif gender == 'kids':
            money_earned += 10
    if haircut == 'color':
        type_of_coloring = input()
        if type_of_coloring == 'touch up':
            money_earned += 20
        elif type_of_coloring == 'full color':
            money_earned += 30
    if money_earned >= target:
        target_achieved = True
        break
    command = input()

if target_achieved:
    print('You have reached your target for the day!')
    print(f'Earned money: {money_earned}lv.')
else:
    print(f'Target not reached! You need {target - money_earned}lv. more.')
    print(f'Earned money: {money_earned}lv.')



