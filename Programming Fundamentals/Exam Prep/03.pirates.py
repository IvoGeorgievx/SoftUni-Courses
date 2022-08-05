def prosper(cities, exploded):
    town = exploded[1]
    gold = int(exploded[2])

    if town in cities:
        if gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")


def plunder(cities, exploded):
    town = exploded[1]
    people = int(exploded[2])
    gold = int(exploded[3])
    if town in cities:
        if cities[town][0] >= 0 and cities[town][1] >= 0:
            cities[town][0] -= people
            cities[town][1] -= gold
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]


def pirates():
    command = input()
    cities = {}

    while command != 'Sail':
        parameters = command.split("||")
        city = parameters[0]
        population = int(parameters[1])
        gold = int(parameters[2])

        if city not in cities:
            cities[city] = [population, gold]
        else:
            cities[city][0] += population
            cities[city][1] += gold

        command = input()

    action = input()

    while action != 'End':
        exploded = action.split("=>")
        current_action = exploded[0]
        if current_action == 'Plunder':
            plunder(cities, exploded)
        elif current_action == 'Prosper':
            prosper(cities, exploded)

        action = input()

    if len(cities) > 0:
        print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")

        for key, value in cities.items():
            print(f"{key} -> Population: {cities[key][0]} citizens, Gold: {cities[key][1]} kg")

    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


pirates()
