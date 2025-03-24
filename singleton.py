from typing import Self


class SingletonMeta(type):
    _instance: Self = None

    def __call__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            instance = super().__call__(*args, **kwargs)
            cls._instance = instance
        return cls._instance


class DatabaseConnection(metaclass=SingletonMeta):
    _initialized = False

    def __init__(self, connection_string: str = "localhost:8080"):
        if not self._initialized:
            self.connection_string = connection_string
            self.connected = False
            self.__class__._initialized = True

    def connect(self):
        if not self.connected:
            print(f"Connecting to database at {self.connection_string}...")
            self.connected = True
        else:
            print("Already connected.")

    def disconnect(self):
        if self.connected:
            print("Disconnecting from database...")
            self.connected = False
        else:
            print("Already disconnected.")

    def status(self):
        return "Connected" if self.connected else "Disconnected"
