from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name

        self.food_menu = []
        self.drink_menu = []
        self.table_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type != 'Bread' and food_type != 'Cake':
            return
        if any(f.name == name for f in self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")
        new_food = ''
        if food_type == 'Bread':
            new_food = Bread(name, price)
        if food_type == 'Cake':
            new_food = Cake(name, price)
        self.food_menu.append(new_food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type != 'Tea' and drink_type != 'Water':
            return
        if any(d.name == name for d in self.drink_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")
        new_drink = ''
        if drink_type == 'Tea':
            new_drink = Tea(name, portion, brand)
        if drink_type == 'Water':
            new_drink = Water(name, portion, brand)
        self.drink_menu.append(new_drink)
        return f"Added {name} ({drink_type}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type != 'InsideTable' and table_type != 'OutsideTable':
            return
        if any(t.table_number == table_number for t in self.table_repository):
            raise Exception(f"Table {table_number} is already in the bakery!")
        new_table = ''
        if table_type == 'InsideTable':
            new_table = InsideTable(table_number, capacity)
        if table_type == 'OutsideTable':
            new_table = OutsideTable(table_number, capacity)
        self.table_repository.append(new_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.table_repository:
            if table.is_reserved:
                continue
            if table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.__find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered_food = f"Table {table_number} ordered:\n"
        skipped_order_food = f'{self.name} does not have in the menu:\n'
        for food_name in food_names:
            food = self.find_food_by_name(food_name)

            if food is None:
                skipped_order_food += food_name + '\n'
            else:
                ordered_food += str(food) + '\n'
        return ordered_food.strip() + '\n' + skipped_order_food.strip()

    def order_drink(self, table_number: int, *drinks_names):
        table = self.__find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered_drinks = f"Table {table_number} ordered:\n"
        skipped_ordered_drinks = f'{self.name} does not have in the menu:\n'
        for drink_name in drinks_names:
            drink = self.find_drink_by_name(drink_name)

            if drink is None:
                skipped_ordered_drinks += drink_name + '\n'
            else:
                ordered_drinks += str(drink) + '\n'
        return ordered_drinks.strip() + '\n' + skipped_ordered_drinks.strip()

    def leave_table(self, table_number: int):
        table = self.__find_table_by_number(table_number)

        bill = table.get_bill()
        self.total_income += bill

        table.clear()
        return f'Table: {table_number}\n' + f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ''
        for table in self.table_repository:
            if not table.is_reserved:
                result += table.free_table_info() + '\n'
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income}lv"

    def __find_table_by_number(self, table_number):
        for table in self.table_repository:
            if table.table_number == table_number:
                return table
        return None

    def find_food_by_name(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food
        return None

    def find_drink_by_name(self, drink_name):
        for drink in self.drink_menu:
            if drink.name == drink_name:
                return drink
        return None
