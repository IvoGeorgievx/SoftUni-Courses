world_record = float(input())
distance_in_metres = float(input())
time_for_one_meter = float(input())

water_resistance = distance_in_metres // 15 * 12.5

total_time = distance_in_metres * time_for_one_meter + water_resistance

if total_time < world_record:
    print(f' Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {abs(world_record - total_time):.2f} seconds slower.')
