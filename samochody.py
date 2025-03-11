from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class Wheel:
    diameter: int
    material: str = field(default="aluminium")


@dataclass
class Body:
    color: str
    thickness: float = field(default=.6)
    type: str = field(default="Sedan") # Suv, Sedan


@dataclass
class Door:
    interior_material: str
    control: str = field(default="manual")


@dataclass
class Seat:
    material: str
    control: str = field(default="manual")


class Factory(ABC):
    @abstractmethod
    def produce_wheels(self, diameter: int, amount: int) -> tuple:
        pass

    @abstractmethod
    def produce_body(self, color: str, type: str) -> Body:
        pass

    @abstractmethod
    def produce_doors(self, interior_material: str, amount: int) -> tuple:
        pass

    @abstractmethod
    def produce_seats(self, material: str, amount: int) -> tuple:
        pass


class TeslaCarFactory(Factory):
    def produce_wheels(self, diameter: int, amount: int) -> tuple:
        return tuple([Wheel(diameter=diameter) for _ in range(amount)])

    def produce_body(self, color: str, type: str) -> Body:
        return Body(color=color, type=type)

    def produce_doors(self, interior_material: str, amount: int) -> tuple:
        return tuple([Door(interior_material=interior_material) for _ in range(amount)])

    def produce_seats(self, material: str, amount: int) -> tuple:
        return tuple([Seat(material=material) for _ in range(amount)])


class BMWCarFactory(Factory):
    def produce_wheels(self, diameter: int, amount: int) -> tuple:
        return tuple([Wheel(diameter=diameter) for _ in range(amount)])

    def produce_body(self, color: str, type: str) -> Body:
        return Body(color=color, thickness=2., type=type)

    def produce_doors(self, interior_material: str, amount: int) -> tuple:
        return tuple([Door(interior_material=interior_material, control="electric") for _ in range(amount)])

    def produce_seats(self, material: str, amount: int) -> tuple:
        return tuple([Seat(material=material) for _ in range(amount)])


class AbstractFactory:
    @staticmethod
    def get_factory(model: Any) -> Any:
        match model:
            case "Tesla":
                return TeslaCarFactory()
            case "BMW":
                return BMWCarFactory
            case _:
                raise ValueError("Incorrect car model")


@dataclass
class Car:
    wheels: tuple
    body: Body
    doors: tuple
    seats: tuple


class CarManufacturer(ABC):
    client_options: dict

    def __init__(self, client_options: dict) -> None:
        self.client_options = client_options

    def produce_car(self) -> Car:
        factory = AbstractFactory.get_factory(self.client_options["model"])
        wheels, body, doors, seats = self._request_parts(factory)

        return Car(wheels=wheels, body=body, doors=doors, seats=seats)

    def _request_parts(self, factory: Any) -> tuple:
        wheels = factory.produce_wheels(self.client_options["diameter"], 4)
        body = factory.produce_body(self.client_options["color"], self.client_options["type"])
        doors = factory.produce_doors(self.client_options["doors"], 5)
        seats = factory.produce_seats(self.client_options["seats"], 5)

        return wheels, body, doors, seats


class Client:
    @staticmethod
    def request_car(request: dict) -> Car:
        manufacturer = CarManufacturer(request)
        new_car = manufacturer.produce_car()

        return new_car


car_specification = {
    "model": "Tesla",
    "diameter": 18,
    "color": "black",
    "doors": "plastic",
    "seats": "normal",
    "type": "SUV"
}

client = Client()
car = client.request_car(car_specification)
print(car)
