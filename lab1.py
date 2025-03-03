from abc import abstractmethod, ABC
from collections import namedtuple
from dataclasses import dataclass, field




class Employee:
    first_name: str
    last_name: str
    salary: float

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return f"I'm {self.first_name} {self.last_name}"


class Manager(Employee):
    department: str

    def __init__(self, first_name: str, last_name: str, salary: float, department: str) -> None:
        super().__init__(first_name, last_name, salary)
        self.department = department

    def get_department_info(self) -> str:
        return f"I manage {self.department}"


class BankAccount:
    balance: float

    def __init__(self) -> None:
        self.balance = 0

    def apply_transaction(self, transaction: namedtuple) -> None:
        self.balance += transaction[1]


@dataclass(frozen=False)
class Book:
    title: str
    author: str
    year: int
    price: float

    def apply_discount(self, procentage: int):
        self.price -= self.price * (procentage / 100)


@dataclass(frozen=False)
class Product:
    name: str
    price: float
    category: str

    def __init__(self, name: str, price: float, category: str = "Genaral") -> None:
        self.name = name
        self.category = category

        if price <= 0:
            raise ValueError("Price cannot be less or equal to zero")
        else:
            self.price = price


class Car:
    brand: str
    model: str
    year: int

    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def is_classic(self) -> bool:
        return True if self.year > 25 else False


class ElectricVehicle:

    def fuel_type(self) -> str:
        return "Electric"


class GasolineVehicle:

    def fuel_type(self) -> str:
        return "Gasoline"


class HybridCar(ElectricVehicle, GasolineVehicle):

    def fuel_type(self) -> str:
        return "Hybrid"


class Person:
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self) -> str:
        return "I am a person"


class Worker(Person):
    occupation: str

    def __int__(self, first_name: str, last_name: str, occupation: str) -> None:
        super().__init__(first_name, last_name)
        self.occupation = occupation

    def introduce(self) -> str:
        return "I am a worker"


class Student(Person):
    specialization: str

    def __int__(self, first_name: str, last_name: str, specialization) -> None:
        super().__init__(first_name, last_name)
        self.specialization = specialization

    def introduce(self) -> str:
        return "I am a student"


class WorkingStudent(Worker, Student):
    pass


class Animal:
    def make_sound(self) -> str:
        return "Some sound"


class Pet:
    def is_domestic(self) -> bool:
        return True


class Dog(Animal, Pet):
    def make_sound(self) -> str:
        return "woof woof ฅ՞•ﻌ•՞ฅ"


class FlyingVehicle:
    def move(self) -> str:
        return "I fly"


class WaterVehicle:
    def move(self) -> str:
        return "I sail"


class AmphibiousVehicle(FlyingVehicle, WaterVehicle):
    def __init__(self, mode: str) -> None:
        self.mode = mode

    def move(self) -> str:
        if self.mode == "fly":
            return FlyingVehicle.move(self)
        elif self.mode == "swim":
            return WaterVehicle.move(self)
        else:
            return "Invalid mode"

class Robot:
    def operate(self) -> str:
        return "Performing task"


class AI:
    def think(self) -> str:
        return "Processing data"


class Android(Robot, AI):
    def self_learn(self) -> str:
        return "?"


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5/9


class IDGenerator:
    id_counter = 0

    @classmethod
    def generate_id(cls) -> int:
        cls.id_counter += 1
        return cls.id_counter


class Store:
    total_customers = 0

    @classmethod
    def add_customer(cls) -> None:
        cls.total_customers += 1

    @classmethod
    def get_total_customers(cls) -> int:
        return cls.total_customers


class MathOperations:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @classmethod
    def identity_matrix(cls, size: int) -> list:
        matrix = []
        for i in range(size):
            temp_row = []
            for j in range(size):
                if i == j:
                    temp_row.append(1)
                else:
                    temp_row.append(0)
            matrix.append(temp_row)

        return matrix


class GameCharacter:
    default_health = 100

    def __init__(self):
        self.health = self.default_health

    def restore_health(self):
        self.health = self.default_health

    @classmethod
    def set_default_health(cls, new_value: int):
        cls.default_health = new_value


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * pow(self.radius, 2)

# 1
employee1 = Employee("Michal", "Kownakci", 0)
manager1 = Manager("Sotomek", "Sotomski", 400.3, "sales")
print(employee1.get_full_name())
print(manager1.get_department_info())

# 2
Transaction = namedtuple("Transaction", ["transaction_id", "amount", "currency"])
transaction1 = Transaction(transaction_id=1, amount=100, currency="Pesos")

BankAcc = BankAccount()
print(BankAcc.balance)
BankAcc.apply_transaction(transaction1)
print(BankAcc.balance)

# 3
book1 = Book("Dziady cz III", "Adam Mickewicz", 1832, 200)
print(book1.price)
book1.apply_discount(10)
print(book1.price)

# 4
product1 = Product("bulka", 0.3)
print(product1.category)

# 5

# 6
hcar = HybridCar()
print(hcar.fuel_type())

# 7
ws = WorkingStudent("Mich", "Kownacki")
print(ws.introduce())

# 8
dogo = Dog()
print(dogo.is_domestic())
print(dogo.make_sound())

# 9
amphibious = AmphibiousVehicle("fly")
print(amphibious.move())

amphibious.mode = "swim"
print(amphibious.move())

# 10

# 11
print(TemperatureConverter.celsius_to_fahrenheit(10))
print(TemperatureConverter.fahrenheit_to_celsius(0))

# 12
print(IDGenerator.generate_id())
print(IDGenerator.generate_id())

# 13
Store.add_customer()
print(Store.get_total_customers())
Store.add_customer()
print(Store.get_total_customers())

# 14
print(MathOperations.add(2, 2))
print(MathOperations.multiply(2, 3))
print(MathOperations.identity_matrix(3))

# 15
char1 = GameCharacter()
print(char1.health)
char1.health = 10
char1.restore_health()
print(char1.health)

GameCharacter.set_default_health(1337)
char2 = GameCharacter()
print(char2.health)

# 16
