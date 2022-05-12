movie_name = input()
student_ticket = 0
standard_ticket = 0
kid_ticket = 0
tickets_total = 0
while movie_name != 'Finish':
    free_seats = int(input())
    seats_taken = 0
    ticket_type = input()
    while ticket_type != 'End':
        if ticket_type == 'student':
            student_ticket += 1
        elif ticket_type == 'standard':
            standard_ticket += 1
        elif ticket_type == 'kid':
            kid_ticket += 1
        seats_taken += 1
        if free_seats - seats_taken == 0:
            break

        ticket_type = input()
    print(f'{movie_name} - { seats_taken / free_seats * 100:.2f}% full.')
    movie_name = input()
all_tickets = kid_ticket + standard_ticket + student_ticket
print(f'Total tickets: {all_tickets}')
print(f'{student_ticket / all_tickets * 100:.2f}% student tickets.')
print(f'{standard_ticket / all_tickets * 100:.2f}% standard tickets.')
print(f'{kid_ticket / all_tickets * 100:.2f}% kids tickets.')



