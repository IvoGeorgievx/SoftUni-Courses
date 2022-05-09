bottles = int(input())
detergent_in_ml = bottles * 750
plate = 5
pot = 15
pot_count = 0
plate_count = 0
refill_counter = 0
required_detergent = 0

while True:
    dishes = input()
    if dishes != 'End':
        dishes = int(dishes)
        refill_counter += 1
    else:
        print('Detergent was enough!')
        print(f'{plate_count} dishes and {pot_count} pots were washed.')
        print(f'Leftover detergent {detergent_in_ml - required_detergent} ml.')
        break
    if refill_counter < 3:
        required_detergent += dishes * plate
        plate_count += dishes
    else:
        pot_count += dishes
        refill_counter = 0
        required_detergent += dishes * pot
        if required_detergent > detergent_in_ml:
            print(f'Not enough detergent, {required_detergent - detergent_in_ml} ml. more necessary!')
            break


