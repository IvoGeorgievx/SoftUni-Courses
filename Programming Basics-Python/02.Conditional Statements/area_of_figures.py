from math import pi

shape = str(input())
result = 0

if shape == "square":
    side = float(input())
    result = side * side
    print(f"{result:.3f}")

elif shape == "rectangle":
    side_a = float(input())
    side_b = float(input())
    result = side_a * side_b
    print(f"{result:.3f}")

elif shape == "circle":
    radius = float(input())
    result = radius ** 2 * pi
    print(f"{result:.3f}")

else:  #shape == "triangle"
    side = float(input())
    height = float(input())
    result = (side * height) / 2
    print(f"{result:.3f}")







