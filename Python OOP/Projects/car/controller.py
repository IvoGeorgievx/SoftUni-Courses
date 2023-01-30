from project73.car.car import Car
from project73.driver import Driver
from project73.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        new_car = Car(model, speed_limit)
        if car_type != 'SportsCar' and car_type != 'MuscleCar':
            return
        if any(c.model == model for c in self.cars):
            raise Exception(f"Car {model} is already created!")
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        new_driver = Driver(driver_name)
        if any(d.name == driver_name for d in self.drivers):
            raise Exception(f"Driver {new_driver.name} is already created!")
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        new_race = Race(race_name)
        if any(r.name == race_name for r in self.races):
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        car = self.__find_last_free_car_by_type(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        return driver.change_car(car)

    def add_driver_to_race(self, race_name: str, driver_name: str):
        pass

    def start_race(self, race_name: str):
        pass

    def __find_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        return None

    def __find_last_free_car_by_type(self, car_type):
        for idx in range(len(self.cars) - 1, -1, -1):
            car = self.cars[idx]

            if not car.is_taken and car.__class__.__name__ == car_type:
                return car
        return None
