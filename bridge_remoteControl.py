from abc import ABC, abstractmethod


class Electronic(ABC):
    name: str
    brand: str
    year: int

    def __init__(self, name: str, brand: str, year: int) -> None:
        self.name = name
        self.brand =brand
        self.year = year

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass


class TV(Electronic):
    name: str
    brand: str
    year: int
    display_type: str
    screen_size: str

    def __init__(self, name: str, brand: str, year: int, display_type: str, screen_size: str):
        super().__init__(name, brand, year)
        self.display_type = display_type
        self.screen_size = screen_size

    def turn_off(self) -> None:
        print("TV off")

    def turn_on(self) -> None:
        print("TV on")

    def change_channel(self, channel: int) -> None:
        print(f"Channel changed to {channel}")


class Radio(Electronic):
    name: str
    brand: str
    year: int
    tuner_type: str
    freq_range: str
    current_freq: float

    def __init__(self, name: str, brand: str, year: int, tuner_type: str, freq_range: str):
        super().__init__(name, brand, year)
        self.tuner_type = tuner_type
        self.freq_range = freq_range
        self.current_freq = 0.0

    def turn_off(self) -> None:
        print("Radio off")

    def turn_on(self) -> None:
        print("Radio on")
    
    def display_current_frequency(self) -> float:
        return self.current_freq
        
    def adjust_frequency(self, frequency: float):
        self.current_freq = frequency
        print(f"Frequency changed from{self.current_freq} to {frequency}")
