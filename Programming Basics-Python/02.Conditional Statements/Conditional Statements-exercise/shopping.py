budget = float(input())
video_cards_count = int(input())
processor_count = int(input())
RAM_count = int(input())

video_card_price = 250
video_card_total = video_card_price * video_cards_count
processor_price = (video_cards_count * video_card_price) * 0.35
processor_total = processor_count * processor_price
RAM_price = (video_cards_count * video_card_price) * 0.10
RAM_total = RAM_count * RAM_price

total_price = RAM_total + processor_total + video_card_total

if video_cards_count > processor_count:
    total_price = total_price - (total_price * 0.15)

if total_price <= budget:
    print(f'You have {budget - total_price:.2f} leva left!')
else:
    print(f'Not enough money! You need {abs(total_price - budget):.2f} leva more!')











