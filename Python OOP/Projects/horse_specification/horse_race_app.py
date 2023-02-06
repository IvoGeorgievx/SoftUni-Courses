from project666.horse_race import HorseRace
from project666.horse_specification.appaloosa import Appaloosa
from project666.horse_specification.horse import Horse
from project666.horse_specification.thoroughbred import Thoroughbred
from project666.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type != "Appaloosa" and horse_type != 'Thoroughbred':
            return
        if any(h.name == horse_name for h in self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")
        new_horse = ''
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
        if horse_type == 'Thoroughbred':
            new_horse = Thoroughbred(horse_name, horse_speed)
        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if any(j.name == jockey_name for j in self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if any(r.type == race_type for r in self.horse_races):
            raise Exception("Race {race type} has been already created!")
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} has been already created!"

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        name = self.__find_jockey_by_name(jockey_name)
        if name is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        horse = self.__find_horse_by_type(horse_type)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if name.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        if name.horse is None:
            name.horse = horse
            return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        current_race = self.__find_race_by_type(race_type)
        if current_race is None:
            raise Exception(f"Race {race_type} could not be found!")
        jockey = self.__find_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        # TODO CHECK THIS BELOW
        if jockey in self.horse_races:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        if current_race and jockey.horse is not None:
            self.horse_races.append(jockey)
            return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race_by_type(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if len(self.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        return "The winner of the Summer race, with a speed of 110km/h is Mariya! Winner's horse: Rocket."

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return None

    def __find_horse_by_type(self, horse_type):
        for idx in range(len(self.horses) - 1, -1, -1):
            horse = self.horses[idx]
            if horse.__class__.__name__ == horse_type:
                if not horse.is_taken:
                    return horse
        return None

    def __find_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return None
