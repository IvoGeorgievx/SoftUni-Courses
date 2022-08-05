lines_count = int(input())
plant_dict = {}
counter = 1

for i in range(lines_count):
    temp_dict = {}
    information = input()
    exploded = information.split("<->")
    plant_name = exploded[0]
    rarity = exploded[1]
    plant_dict[plant_name] = {rarity}
    temp_dict['rarity'] = rarity
    temp_dict['rating'] = 0
    plant_dict[plant_name] = temp_dict


command = input()

while command != 'Exhibition':

    counter = 1
    exploded = command.split(": ")
    action = exploded[0]

    if action == 'Rate':
        ratings = []
        everything_else = exploded[1].split(" - ")
        plant = everything_else[0]
        rating = int(everything_else[1])
        if plant in plant_dict:
            plant_dict[plant]['rating'] += int(rating)
            ratings.append(rating)
        else:
            print('error')

    elif action == 'Update':
        everything_else = exploded[1].split(" - ")
        plant = everything_else[0]
        new_rarity = everything_else[1]
        if plant in plant_dict:
            plant_dict[plant]['rarity'] = new_rarity
        else:
            print('error')

    elif action == 'Reset':
        plant = exploded[1]
        if plant in plant_dict:
            plant_dict[plant]['rating'] = 0
        else:
            print('error')

    command = input()

print("Plants for the exhibition:")

for key, value in plant_dict.items():
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {value['rating']:.2f}")

