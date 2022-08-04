def heal(hero_dict, exploded):
    hero_name = exploded[1]
    amount = int(exploded[2])

    if hero_name in hero_dict:
        recovered = 100 - hero_dict[hero_name][0]
        hero_dict[hero_name][0] += amount
        if hero_dict[hero_name][0] > 100:
            hero_dict[hero_name][0] = 100
            print(f"{hero_name} healed for {recovered} HP!")
        else:
            print(f"{hero_name} healed for {amount} HP!")

    return hero_dict


def recharge(hero_dict, exploded):
    hero_name = exploded[1]
    amount = int(exploded[2])

    if hero_name in hero_dict:
        recovered = 200 - hero_dict[hero_name][1]
        hero_dict[hero_name][1] += amount
        if hero_dict[hero_name][1] > 200:
            hero_dict[hero_name][1] = 200
            print(f"{hero_name} recharged for {recovered} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")

    return hero_dict


def take_damage(hero_dict, exploded):
    hero_name = exploded[1]
    damage = int(exploded[2])
    attacker = exploded[3]

    if hero_name in hero_dict:
        if hero_dict[hero_name][0] - damage > 0:
            hero_dict[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_dict[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            hero_dict.pop(hero_name)

    return hero_dict


def cast_spell(hero_dict, exploded):
    hero_name = exploded[1]
    mp_needed = int(exploded[2])
    spell_name = exploded[3]

    if hero_name in hero_dict:
        if hero_dict[hero_name][1] - mp_needed >= 0:
            hero_dict[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero_dict[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    return hero_dict


def heroes_of_code_logic():
    number_of_heroes = int(input())
    hero_dict = {}

    for i in range(number_of_heroes):
        info = input()
        exploded = info.split(" ")
        hero_name = exploded[0]
        hero_hp = int(exploded[1])
        hero_mp = int(exploded[2])
        hero_dict[hero_name] = [hero_hp, hero_mp]

    command = input()

    while command != 'End':
        exploded = command.split(" - ")
        action = exploded[0]

        if action == 'CastSpell':
            cast_spell(hero_dict, exploded)
        elif action == 'TakeDamage':
            take_damage(hero_dict, exploded)
        elif action == 'Recharge':
            recharge(hero_dict, exploded)
        elif action == 'Heal':
            heal(hero_dict, exploded)

        command = input()

    for key, value in hero_dict.items():
        print(f'{key}\n  HP: {hero_dict[key][0]} \n  MP: {hero_dict[key][1]}')


heroes_of_code_logic()
