from dataclasses import dataclass
from copy import deepcopy
from copy import copy
from typing import Any, Self
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name: str, health: int, race: str, resource: int, level: int = 1):
        self.name = name
        self.health = health
        self.resource = resource
        self.level = level
        self.race = race
        self.specialisation = ""
        self.checklist = [1, 2]

    def char_info(self) -> str:
        return (f"I am {self.name}, level {self.level} {self.race} {self.specialisation}"
                f", with {self.health} health points and {self.resource} resource points")

    @abstractmethod
    def do_action(self, ability) -> str:
        pass


class Prototype(ABC):
    @abstractmethod
    def shallow_clone(self) -> Self:
        pass

    @abstractmethod
    def deep_clone(self) -> Self:
        pass


class Mage(Character, Prototype):
    def __init__(self, name: str, health: int, race: str, resource: int, level: int):
        super().__init__(name, health, race, resource, level)
        self.specialisation = "Mage"

    def do_action(self, ability: str) -> str:
        return f"I cast {ability} using mana"

    def shallow_clone(self) -> Self:
        return copy(self)

    def deep_clone(self) -> Self:
        return deepcopy(self)


class Warrior(Character, Prototype):
    def __init__(self, name: str, health: int, race: str, resource: int, level: int):
        super().__init__(name, health, race, resource, level)
        self.specialisation = "Warrior"

    def do_action(self, ability: str) -> str:
        return f"I cast {ability} using rage"

    def shallow_clone(self) -> Self:
        return copy(self)

    def deep_clone(self) -> Self:
        return deepcopy(self)


mag = Mage("Gandalf", 100, "human", 1000, 50)
print(mag.char_info())
print(mag.do_action("Fireball"))

woj = Warrior("Gromash", 1000, "orc", 100, 70)
print(woj.char_info())
print(woj.do_action("Heroic Strike"))

print("------------")

mag_clone = mag.shallow_clone()
mag_deepclone = mag.deep_clone()
print("Mag orginal check list", mag.checklist)
print("Mag_clone(shallow) cloned check list", mag_clone.checklist)
mag_clone.checklist[0] = 10
mag_deepclone.checklist[1] = 12
print("Mag orginal check list after change", mag.checklist)
print("Mag_clone(shallow) cloned check list after change", mag_clone.checklist)
print("Mag_deepclone(deep) cloned check list after change", mag_deepclone.checklist)
