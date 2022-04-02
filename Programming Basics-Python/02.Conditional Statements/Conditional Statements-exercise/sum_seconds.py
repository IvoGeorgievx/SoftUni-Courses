#Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50).
# Да се напише програма, която чете времената на състезателите в секунди,
# въведени от потребителя и пресмята сумарното им време във формат "минути:секунди".
# Секундите да се изведат с водеща нула (2  "02", 7  "07", 35  "35").
from math import floor


racer_1 = float(input())
racer_2 = float(input())
racer_3 = float(input())

race_total = racer_1 + racer_2 + racer_3
minutes = race_total // 60
seconds = race_total % 60
minutes = floor(minutes)
seconds = floor(seconds)
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
