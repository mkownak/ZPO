from abc import ABC


class SmartAppliance(ABC):
    type: str
    status: bool

    @staticmethod
    def turn_on():
        pass

    @staticmethod
    def turn_off():
        pass


class Heater(SmartAppliance):
    temp: float

    def __init__(self):
        self.temp = 21.0
        self.type = "heating"
        self.status = False

    def turn_on(self):
        self.status = True
        print("Heating On")

    def turn_off(self):
        self.status = False
        print("Heating off")

    def check_status(self):
        return self.status

    def change_temp(self, temp):
        self.temp = temp


class Lights(SmartAppliance):
    brightness_percentage: float

    def __init__(self):
        self.brightness_percentage = 0.75
        self.type = "light"
        self.status = False

    def turn_on(self):
        self.status = True
        print("Lights On")

    def turn_off(self):
        self.status = False
        print("Lights off")

    def check_status(self):
        return self.status

    def change_brightness(self, brighntess):
        self.brightness_percentage = brighntess


class SmartHome:
    appliances: list

    def __init__(self):
