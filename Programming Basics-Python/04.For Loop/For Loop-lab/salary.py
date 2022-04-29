tabs_opened = int(input())
salary = int(input())

facebook = 150
instagram = 100
reddit = 50

for tabs in range(tabs_opened):
    tab_name = input()
    if tab_name == 'Facebook':
        salary -= facebook
    elif tab_name == 'Instagram':
        salary -= instagram
    elif tab_name == 'Reddit':
        salary -= reddit
if salary <= 0:
    print("You have lost your salary.")
if salary > 0:
    print(salary)
