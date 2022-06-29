def print_func(legendary_materials, junk_materials, special_item):
    print(f"{special_item} obtained!")
    print(f"shards: {legendary_materials['shards']}")
    print(f"fragments: {legendary_materials['fragments']}")
    print(f"motes: {legendary_materials['motes']}")

    for key, value in junk_materials.items():
        print(f"{key}: {value}")


def legendary_farming():

    legendary_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
    junk_materials = {}
    condition = False

    while True:
        items = input().lower()
        items = items.split(" ")

        for value, material in zip(items[0::2], items[1::2]):
            material = material.lower()
            value = int(value)
            special_item = ''
            if material in legendary_materials:
                if material == 'shards':
                    legendary_materials[material] += value
                    if legendary_materials[material] >= 250:
                        legendary_materials[material] -= 250
                        special_item = 'Shadowmourne'
                        condition = True
                        print_func(legendary_materials, junk_materials, special_item)

                elif material == 'fragments':
                    legendary_materials[material] += value
                    if legendary_materials[material] >= 250:
                        legendary_materials[material] -= 250
                        special_item = 'Valanyr'
                        condition = True
                        print_func(legendary_materials, junk_materials, special_item)

                elif material == 'motes':
                    legendary_materials[material] += value
                    if legendary_materials[material] >= 250:
                        legendary_materials[material] -= 250
                        special_item = 'Dragonwrath'
                        condition = True
                        print_func(legendary_materials, junk_materials, special_item)
            else:
                if material not in junk_materials:
                    junk_materials[material] = value
                else:
                    junk_materials[material] += value

            if condition:
                break
        if condition:
            break


legendary_farming()
