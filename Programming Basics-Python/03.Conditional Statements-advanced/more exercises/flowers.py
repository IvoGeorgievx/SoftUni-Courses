chrysanthemas_count = int(input())
roses_count = int(input())
tulip_count = int(input())
season = input()
holiday = input()

chysanthemas_price = 0
roses_price = 0
tulip_price = 0
total_price = 0
total_count = chrysanthemas_count + roses_count + tulip_count
if season == 'Spring' or season == 'Summer':
    chysanthemas_price = 2.00
    roses_price = 4.10
    tulip_price = 2.50
    total_price = (chysanthemas_price * chrysanthemas_count) + (roses_count * roses_price) \
                  + (tulip_price * tulip_count)
    if holiday == 'Y':
        total_price = total_price + (total_price * 0.15)
    if season == 'Spring' and tulip_count > 7:
        total_price = total_price - (total_price * 0.05)
    if total_count > 20:
        total_price = total_price - (total_price * 0.2)

if season == 'Autumn' or season == 'Winter':
    chysanthemas_price = 3.75
    roses_price = 4.50
    tulip_price = 4.15
    total_price = (chysanthemas_price * chrysanthemas_count) + (roses_count * roses_price) \
                  + (tulip_price * tulip_count)
    if holiday == 'Y':
        total_price = total_price + (total_price * 0.15)
    if season == 'Winter' and roses_count >= 10:
        total_price = total_price - (total_price * 0.1)
    if total_count > 20:
        total_price = total_price - (total_price * 0.2)

total_price += 2
print(f'{total_price:.2f}')
