fuel_type = input()
fuel_litres = float(input())
card = input()

gasoline = 2.22
diesel = 2.33
gas = 0.93

total_price = 0

if fuel_type == 'Gasoline':
    if card == 'Yes':
        gasoline = gasoline - 0.18
    elif card == 'No':
        gasoline = gasoline
    if 20 <= fuel_litres <= 25:
        total_price = gasoline * fuel_litres - (gasoline * fuel_litres * 0.08)
    elif fuel_litres > 25:
        total_price = gasoline * fuel_litres - (gasoline * fuel_litres * 0.1)
    else:
        total_price = gasoline * fuel_litres

elif fuel_type == 'Diesel':
    if card == 'Yes':
        diesel = diesel - 0.12
    elif card == 'No':
        diesel = diesel
    if 20 <= fuel_litres <= 25:
        total_price = diesel * fuel_litres - (diesel * fuel_litres * 0.08)
    elif fuel_litres > 25:
        total_price = diesel * fuel_litres - (diesel * fuel_litres * 0.1)
    else:
        total_price = diesel * fuel_litres

elif fuel_type == 'Gas':
    if card == 'Yes':
        gas = gas - 0.08
    elif card == 'No':
        gas = gas
    if 20 <= fuel_litres <= 25:
        total_price = gas * fuel_litres - (gas * fuel_litres * 0.08)
    elif fuel_litres > 25:
        total_price = gas * fuel_litres - (gas * fuel_litres * 0.1)
    else:
        total_price = gas * fuel_litres
print(f'{total_price:.2f} lv.')
