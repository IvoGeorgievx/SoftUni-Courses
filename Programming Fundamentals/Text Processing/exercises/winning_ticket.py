def winning_ticket(text):

    win_ticket = False
    jackpot = False
    special_char = '@#$^'
    win_s_counter = 0

    for ticket in info:
        is_valid = False
        current_ticket = ticket
        current_special_symbol = ''

        if len(current_ticket) == 20:
            is_valid = True
        else:
            print("invalid ticket")
        if is_valid:
            counter = 0
            left_side = current_ticket[:10]
            right_side = current_ticket[10:]
            for ch in left_side:
                if ch != current_special_symbol:
                    counter = 0
                if ch in special_char:
                    current_special_symbol = ch
                    counter += 1
                    if 6 <= counter < 10:
                        win_s_counter = 6
                        win_ticket = True
                    if counter == 10:
                        jackpot = True
                        win_ticket = False
                        break
                else:
                    counter = 0
            counter = 0
            for ch in right_side:
                if ch != current_special_symbol:
                    counter = 0
                if ch in special_char:
                    current_special_symbol = ch
                    counter += 1
                    if 6 <= counter < 10:
                        win_s_counter = 6
                        win_ticket = True
                    if counter == 10:
                        jackpot = True
                        win_ticket = False
                        break
                else:
                    counter = 0
            if win_ticket:
                print(f'ticket "{ticket}" - {win_s_counter}{current_special_symbol}')
            elif jackpot:
                print(f'ticket "{ticket}" - {counter}{current_special_symbol} Jackpot!')
            else:
                print(f'ticket "{ticket}" - no match')


ticket_info = input()
info = [x.strip() for x in ticket_info.split(',')]
winning_ticket(info)
