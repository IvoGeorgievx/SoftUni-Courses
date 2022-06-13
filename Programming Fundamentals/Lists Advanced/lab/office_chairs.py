def office_management(number_of_rooms):
    condition = True
    chairs_left = 0
    for room_number in range(1, number_of_rooms + 1):
        data = input().split(" ")
        available_chairs = len(data[0])
        visitors = int(data[1])
        diff = abs(available_chairs - visitors)

        if visitors > available_chairs:
            print(f"{diff} more chairs needed in room {room_number}")
            condition = False
        elif available_chairs > visitors:
            chairs_left += diff

    if condition:
        print(f"Game On, {chairs_left} free chairs left")


info = int(input())
office_management(info)
