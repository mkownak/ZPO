from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod

    def make_sound(self) -> str:
        pass


class Dog(Animal):
    def make_sound(self) -> str:
        return "bark"

class Cat(Animal):
    def make_sound(self) -> str:
        return "meow"

class AnimalFactory:

    @staticmethod
    def create_animal(parameter):
        if parameter == "dog":
            return Dog()
        elif parameter == "cat":
            return Cat()
        else:
            raise ValueError("unkown parameter")

class DynamicAnimalFactory:

    animal_dict = {}

    def register_animal(self, animal_name:str, animal_class)->None:
        if issubclass(animal_class, Animal) and animal_name not in self.animal_dict:
            self.animal_dict[animal_name] = animal_class
        else:
            raise ValueError("unknown animal class")

    def create_animal(self, parameter):
        if parameter in self.animal_dict:
            return self.animal_dict[parameter]()
        else:
            raise ValueError("unknown animal")

    def show_dict(self):
        return self.animal_dict


DynamicFactory = DynamicAnimalFactory()
DynamicFactory.register_animal("dog", Dog)
dogo = DynamicFactory.create_animal("dog")
print(dogo.make_sound())
print(DynamicFactory.show_dict())
