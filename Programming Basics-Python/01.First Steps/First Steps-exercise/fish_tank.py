lenght = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume_of_aquarium = lenght * width * height
volume_in_litres = volume_of_aquarium / 1000
percentage_total = percentage * 0.01
litres_required = volume_in_litres * (1 - percentage_total)

print(litres_required)



