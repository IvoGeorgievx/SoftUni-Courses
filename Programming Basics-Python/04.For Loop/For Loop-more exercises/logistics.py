cargo_count = int(input())
cargo_weight = 0

bus_price = 200
truck_price = 175
train_price = 120
bus_total = 0
truck_total = 0
train_total = 0
cargo_total = 0
bus_price_total = 0
truck_price_total = 0
train_price_total = 0
total_price = 0
cargo_price = 0
average_per_ton = 0
bus_average = 0
truck_average = 0
train_average = 0

for n in range(1, cargo_count + 1):
    cargo_weight = int(input())
    if cargo_weight <= 3:
        bus_total += cargo_weight
        bus_price_total += cargo_weight * bus_price
    elif 4 <= cargo_weight <= 11:
        truck_total += cargo_weight
        truck_price_total += cargo_weight * truck_price
    elif cargo_weight >= 12:
        train_total += cargo_weight
        train_price_total += cargo_weight * train_price
    cargo_weight = bus_total + truck_total + train_total
    total_price = train_price_total + truck_price_total + bus_price_total
    average_per_ton = total_price / cargo_weight
    bus_average = bus_total / cargo_weight * 100
    truck_average = truck_total / cargo_weight * 100
    train_average = train_total / cargo_weight * 100
print(f'{average_per_ton:.2f}')
print(f'{bus_average:.2f}%')
print(f'{truck_average:.2f}%')
print(f'{train_average:.2f}%')
















