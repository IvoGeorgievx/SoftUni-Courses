from abc import ABC, abstractmethod


class Car(ABC):
    MIN_LENGTH = 4

    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < self.MIN_LENGTH:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value


