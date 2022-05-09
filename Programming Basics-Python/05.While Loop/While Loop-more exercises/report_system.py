money_needed = int(input())
cash = 0
card = 0
cash_card_count = 1
total_money = 0
card_counter = 0
cash_counter = 0

while True:
    donated_money = input()
    if donated_money != 'End':
        donated_money = int(donated_money)
    else:
        print('Failed to collect required money for charity.')
        break
    if cash_card_count == 1:
        if donated_money <= 100:
            cash += donated_money
            cash_counter += 1
            print('Product sold!')
        else:
            print('Error in transaction!')

    if cash_card_count == 2:
        cash_card_count = 0
        if donated_money >= 10:
            card += donated_money
            card_counter += 1
            print('Product sold!')
        else:
            print('Error in transaction!')

    total_money = cash + card
    cash_card_count += 1
    if total_money >= money_needed:
        average_cash = cash / card_counter
        average_card = card / card_counter
        print(f'Average CS: {average_cash:.2f}')
        print(f'Average CC: {average_card:.2f}')
        break

