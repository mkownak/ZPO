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
