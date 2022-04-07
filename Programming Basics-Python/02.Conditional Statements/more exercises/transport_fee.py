kilometers = int(input())
time_of_the_day = input()

starting_tax_fee = 0.70
taxi_day_fee = 0.79
taxi_night_fee = 0.90
bus_fee = 0.09
train_fee = 0.06
taxi_price = 0
bus_price = 0
train_price = 0

if time_of_the_day == 'day' and kilometers < 20:
    taxi_price = starting_tax_fee + taxi_day_fee * kilometers
    print(f'{taxi_price:.2f}')
elif time_of_the_day == 'night' and kilometers < 20:
    taxi_price = starting_tax_fee + taxi_night_fee * kilometers
    print(f'{taxi_price:.2f}')
elif 20 <= kilometers < 100:
    bus_price = bus_fee * kilometers
    print(f'{bus_price:.2f}')
elif kilometers >= 100:
    train_price = train_fee * kilometers
    print(f'{train_price:.2f}')




