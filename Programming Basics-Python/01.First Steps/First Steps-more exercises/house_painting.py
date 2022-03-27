x = float(input())
y = float(input())
h = float(input())

front_wall = x * x
back_wall = x * x
door = 1.2 * 2
side_wall_1 = x * y
side_wall_2 = x * y
side_wall_windows = 1.5 * 1.5 * 2
roof_side_1 = x * y
roof_side_2 = x * y
triangle_1 = x * h / 2
triangle_2 = x * h / 2

green_paint_total = (front_wall + back_wall + side_wall_1 + side_wall_2 - door - side_wall_windows) / 3.4
red_paint_total = (roof_side_1 + roof_side_2 + triangle_1 + triangle_2) / 4.3
print(f"{green_paint_total:.2f}")
print(f"{red_paint_total:.2f}")

