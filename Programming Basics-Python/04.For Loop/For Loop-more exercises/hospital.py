period = int(input())
patients_per_day = 0

checked_patients = 0
unchecked_patients = 0
doctors = 7

for n in range(1, period + 1):
    patients_per_day = int(input())
    if patients_per_day <= 7:
        checked_patients += patients_per_day
    elif patients_per_day > 7:
        unchecked_patients += patients_per_day





