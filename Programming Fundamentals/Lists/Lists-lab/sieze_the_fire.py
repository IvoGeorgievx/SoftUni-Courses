fire_cells = input().split("#")
water_amount = int(input())
effort = 0
total_fire = 0
fire_is_valid = False

print('Cells:')
for current_fire in fire_cells:
    fire_info = current_fire.split(" = ")
    type_of_fire = fire_info[0]
    value_of_fire = fire_info[1]
    fire_is_valid = False

    if type_of_fire == 'High':
        if 81 <= int(value_of_fire) <= 125:
            fire_is_valid = True
    elif type_of_fire == 'Medium':
        if 51 <= int(value_of_fire) <= 80:
            fire_is_valid = True
    elif type_of_fire == 'Low':
        if 1 <= int(value_of_fire) <= 50:
            fire_is_valid = True

    if fire_is_valid:
        if water_amount >= int(value_of_fire):
            effort += int(value_of_fire) * 0.25
            water_amount -= int(value_of_fire)
            total_fire += int(value_of_fire)
            print(f' - {int(value_of_fire)}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')