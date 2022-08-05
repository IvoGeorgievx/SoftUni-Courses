number_of_cars = int(input())
car_dict = {}

for i in range(number_of_cars):
    info = input().split("|")
    car = info[0]
    mileage = int(info[1])
    fuel = int(info[2])
    car_dict[car] = [mileage, fuel]

command = input()

while command != 'Stop':
    exploded = command.split(" : ")
    current_command = exploded[0]

    if current_command == 'Drive':
        car = exploded[1]
        distance = int(exploded[2])
        fuel = int(exploded[3])
        if car in car_dict:
            if car_dict[car][1] <= fuel:
                print('Not enough fuel to make that ride')
            else:
                car_dict[car][0] += distance
                car_dict[car][1] -= fuel
                print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
                if car_dict[car][0] >= 100000:
                    print(f'Time to sell the {car}!')

    elif current_command == 'Refuel':
        car = exploded[1]
        fuel = int(exploded[2])
        if car in car_dict:
            current_fuel = 75 - car_dict[car][1]
            car_dict[car][1] += fuel
            if car_dict[car][1] > 75:
                car_dict[car][1] = 75
                print(f'{car} refueled with {current_fuel} liters')
            else:
                print(f"{car} refueled with {fuel} liters")

    elif current_command == 'Revert':
        car = exploded[1]
        km = int(exploded[2])
        if car in car_dict:
            car_dict[car][0] -= km
            if car_dict[car][0] < 10000:
                car_dict[car][0] = 10000
            else:
                print(f"{car} mileage decreased by {km} kilometers")

    command = input()

for key, value in car_dict.items():
    if car_dict[key][0] < 100000:
        print(f'{key} -> Mileage: {car_dict[key][0]} kms, Fuel in the tank: {car_dict[key][1]} lt.')