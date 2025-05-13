from abc import ABC, abstractmethod


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

    def __init__(self):
        self.heating = Heater()
        self.lights = Lights()

    def show_status(self):
        print("Status of heater: ", self.heating.check_status())
        print("status of lights: ", self.lights.check_status())


class Command:
    @abstractmethod
    def execute(self):
        pass


class TurnOnCommand(Command):
    def __init__(self, appliance: SmartAppliance):
        self.appliance = appliance

    def execute(self):
        self.appliance.turn_on()


class TurnOffCommand(Command):
    def __init__(self, appliance: SmartAppliance):
        self.appliance = appliance

    def execute(self):
        self.appliance.turn_off()


class Remote:
    def __init__(self):
        self._commands = []

    def press_button(self, command: Command):
        self._commands.append(command)
        command.execute()

    def show_history(self):
        for command in self._commands:
            print(command)


home = SmartHome()
remote = Remote()

heater_on = TurnOnCommand(home.heating)
heater_off = TurnOffCommand(home.heating)

lights_on = TurnOnCommand(home.lights)
lights_off = TurnOffCommand(home.lights)

home.show_status()

remote.press_button(heater_on)

home.show_status()

remote.show_history()

remote.press_button(lights_off)

