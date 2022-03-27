skum_price = float(input())
kaya_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
clam_kg = int(input())

palamud_price = skum_price + (skum_price * 0.6)
safrid_price = kaya_price + (kaya_price * 0.8)
clam_price = 7.5
palamud_total = palamud_price * palamud_kg
safrid_total = safrid_price * safrid_kg
clam_total = clam_kg * clam_price
total = palamud_total + safrid_total + clam_total
print(f'{total:.2f}')





