# Напишете програма, която познава дали е топло или студено навън.
# От конзолата се чете един ред – текст, който подсказва какво е времето.
# При въвеждане на "sunny" трябва да се отпечата
# "It's warm outside!".
# Във всички останали случаи трябва да се отпечата "It's cold outside!".

weather = str(input())

if weather == "sunny":
    print(f"It's warm outside!")
elif weather == "cloudy":
    print("It's cold outside!")
else:
    print("It's cold outside!")