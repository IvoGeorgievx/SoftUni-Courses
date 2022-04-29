groups_of_climbers = int(input())
climbers_in_group = 0
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for number in range(1, groups_of_climbers + 1):
    climbers_in_group = int(input())
    if climbers_in_group <= 5:
        musala += climbers_in_group
    elif 6 <= climbers_in_group <= 12:
        monblan += climbers_in_group
    elif 13 <= climbers_in_group <= 25:
        kilimanjaro += climbers_in_group
    elif 26 <= climbers_in_group <= 40:
        k2 += climbers_in_group
    elif climbers_in_group >= 41:
        everest += climbers_in_group
climbers_in_group = musala + monblan + kilimanjaro + k2 + everest

musala_percent = musala / climbers_in_group * 100
monblan_percent = monblan / climbers_in_group * 100
kilimanjaro_percent = kilimanjaro / climbers_in_group * 100
k2_percent = k2 / climbers_in_group * 100
everest_percent = everest / climbers_in_group * 100
print(f'{musala_percent:.2f}%')
print(f'{monblan_percent:.2f}%')
print(f'{kilimanjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')




