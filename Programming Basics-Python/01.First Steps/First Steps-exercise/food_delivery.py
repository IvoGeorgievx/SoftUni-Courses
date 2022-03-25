chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15

chicken_menu_sum = int(input())
fish_menu_sum = int(input())
vegetarian_menu_sum = int(input())

chicken_menu_total = chicken_menu_sum * chicken_menu
fish_menu_total = fish_menu_sum * fish_menu
vegetarian_menu_total = vegetarian_menu_sum * vegetarian_menu
total_price_of_menus = chicken_menu_total + fish_menu_total + vegetarian_menu_total
dessert = (chicken_menu_total + fish_menu_total + vegetarian_menu_total) * 0.2
delivery_fee = 2.50
total_price = delivery_fee + dessert + total_price_of_menus
print (total_price)

