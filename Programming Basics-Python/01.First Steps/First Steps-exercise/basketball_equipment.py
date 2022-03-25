# ⦁	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# ⦁	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# ⦁	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# ⦁	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

annual_fare = float(input())

sneakers = annual_fare - (annual_fare * 0.4)
jersey = sneakers - (sneakers * 0.2)
ball = jersey * 0.25
accesories = ball * 0.2

total = sneakers + jersey + ball + accesories + annual_fare
print(total)

