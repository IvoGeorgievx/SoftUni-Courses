fuel_type = input()
fuel_litres = float(input())

if fuel_type == 'Diesel' and fuel_litres >= 25:
    print('You have enough diesel.')
elif fuel_type == 'Diesel' and fuel_litres < 25:
    print('Fill your tank with diesel!')
elif fuel_type == 'Gasoline' and fuel_litres >= 25:
    print('You have enough gasoline.')
elif fuel_type == 'Gasoline' and fuel_litres < 25:
    print('Fill your tank with gasoline!')
elif fuel_type == 'Gas' and fuel_litres >= 25:
    print('You have enough gas.')
elif fuel_type == 'Gas' and fuel_litres < 25:
    print('Fill your tank with gas!')
elif fuel_type != 'Diesel' or fuel_type != 'Gasoline' \
        or fuel_type != 'Gas':
    print('Invalid fuel!')
