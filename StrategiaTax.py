from abc import ABC, abstractmethod


class Ware:
    name: str
    value: float

    def __init__(self, name: str, value: int, country: str) -> None:
        self.name = name
        self.value = value
        self.country = country

    def __str__(self):
        return self.name + " " + str(self.value)


class Strategy(ABC):
    taxation: int

    def __init__(self, taxation: int) -> None:
        self.taxation = taxation

    @abstractmethod
    def calculate_tax(self, value: float) -> float:
        pass


class PolandTax(Strategy):
    # taxation = 23

    def calculate_tax(self, value: float) -> float:
        return value * (self.taxation/100)


class AmericanTax(Strategy):
    # taxation = 10

    def calculate_tax(self, value: float) -> float:
        return value * (self.taxation/100)


class TaxChooser:
    ware: Ware

    def __init__(self, ware: Ware):
        self.ware = ware
        self.strategy = None

    def _chose_strategy(self) -> None:
        if self.ware.country == "Poland":
            self.strategy = PolandTax(23)
        else:
            self.strategy = AmericanTax(10)

    def calculate_tax(self) -> float:
        if self.strategy is None:
            self._chose_strategy()

        if self.ware.country == "Poland":
            return self.strategy.calculate_tax(self.ware.value)

        if self.ware.country == "America":
            return self.strategy.calculate_tax(self.ware.value)


t1 = Ware("Towiec", 150, "America")
calculator = TaxChooser(t1)
print(calculator.calculate_tax())
