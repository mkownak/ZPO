from abc import ABC, abstractmethod


class Smartphone(ABC):
    def __init__(self,brand: str, model: str, battery_capacity: float, ram: int, storage: int, camera: float):
        self.brand: str = brand
        self.model: str = model
        self.battery_capacity :float = battery_capacity
        self.RAM: int = ram
        self.storage: int = storage
        self.camera: float = camera

    def info(self):
        print(f"This is a model {self.model} by {self.brand} with {self.battery_capacity} mAh battery, {self.RAM}GB RAM, {self.storage}GB of storage and {self.camera}MP camera")


class ApfelPhone(Smartphone):
    pass

class SzajsungPhone(Smartphone):
    pass

class MajfonPhone(Smartphone):
    pass

class SmartphoneFactory(ABC):
    @abstractmethod
    def create_apfel(self,specs:dict):
        pass

    @abstractmethod
    def create_szajsung(self,specs:dict):
        pass

    @abstractmethod
    def create_majfon(self,specs:dict):
        pass

class ConcreteSmartphoneFactory(SmartphoneFactory):
    def create_apfel(self,specs:dict):
        return ApfelPhone(**specs)

    def create_szajsung(self,specs:dict):
        return SzajsungPhone(**specs)

    def create_majfon(self,specs:dict):
        return  MajfonPhone(**specs)


apfel_models = {
    "2024": {"brand": "Apfel", "model": "16", "battery_capacity": 3561, "ram": 8, "storage": 256, "camera": 24},
    "2023": {"brand": "Apfel", "model": "15", "battery_capacity": 3349, "ram": 6, "storage": 128, "camera": 48},
    "2022": {"brand": "Apfel", "model": "14", "battery_capacity": 3279, "ram": 6, "storage": 128, "camera": 12},
}

factory = ConcreteSmartphoneFactory()
smartphones = []

for release_year, specs in apfel_models.items():
    smartphones.append(factory.create_apfel(specs))

for phone in smartphones:
    phone.info()
