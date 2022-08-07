vehicles = input().split(">>")
initial_tax = 0
total_revenue = 0

while len(vehicles) > 0:
    current_element = vehicles[0]
    exploded = current_element.split(" ")
    car_type = exploded[0]
    years_in_use = int(exploded[1])
    traveled = int(exploded[2])

    if car_type == 'family':
        initial_tax = 50
        year_used_tax = 5 * years_in_use
        km_tax = traveled // 3000 * 12
        total_tax = km_tax + (initial_tax - year_used_tax)
        total_revenue += total_tax
        print(f"A {car_type} car will pay {total_tax:.2f} euros in taxes.")

    elif car_type == 'heavyDuty':
        initial_tax = 80
        year_used_tax = 8 * years_in_use
        km_tax = traveled // 9000 * 14
        total_tax = km_tax + (initial_tax - year_used_tax)
        total_revenue += total_tax
        print(f"A {car_type} car will pay {total_tax:.2f} euros in taxes.")

    elif car_type == 'sports':
        initial_tax = 100
        year_used_tax = 9 * years_in_use
        km_tax = traveled // 2000 * 18
        total_tax = km_tax + (initial_tax - year_used_tax)
        total_revenue += total_tax
        print(f"A {car_type} car will pay {total_tax:.2f} euros in taxes.")
    else:
        print("Invalid car type.")

    vehicles.remove(current_element)


print(f'The National Revenue Agency will collect {total_revenue:.2f} euros in taxes.')

