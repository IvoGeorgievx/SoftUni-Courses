month = input()
nights = int(input())
apartment = 0
studio = 0
total_price_apartment = 0
total_price_studio = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if 7 < nights <= 14:
        studio = studio - (studio * 0.05)
    elif 14 < nights:
        studio = studio - (studio * 0.3)
    total_price_apartment = nights * apartment
    total_price_studio = nights * studio
elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
    if 14 < nights:
        studio = studio - (studio * 0.2)
    total_price_apartment = nights * apartment
    total_price_studio = nights * studio

elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
if 14 < nights:
    apartment = apartment - (apartment * 0.1)
total_price_apartment = nights * apartment
total_price_studio = nights * studio
print(f'Apartment: {total_price_apartment:.2f} lv.') 
print(f'Studio: {total_price_studio:.2f} lv.')





