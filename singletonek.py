from typing import Self


class SingletonMeta(type):
    _instance: Self = None

    def __call__(cls, *args: list, **kwargs: dict) -> Self:
        if cls._instance is None:
            instance = super().__call__(*args, **kwargs)
            cls._instance = instance

        return cls._instance


class DatabaseConnection(metaclass=SingletonMeta):
    _check: dict = {"$servername": "127.0.0.1",
                    "$username": "Kownak",
                    "$password": "1234"}

    def __init__(self, connection_parameters: dict) -> None:
        self._servername = connection_parameters["$servername"]
        self._username = connection_parameters["$username"]
        self._password = connection_parameters["$password"]
        self._connection_status = False

    def connect(self) -> str:
        if self._connection_status:
            return "Already connected to database"

        if (self._servername == self._check["$servername"] and
                self._username == self._check["$username"] and
                self._password == self._check["$password"]):
            self._connection_status = True
            return "Connected successfully"
        else:
            return "Connection failed"

    def disconnect(self) -> str:
        self._connection_status = False
        return "Connection terminated"

    def check_status(self) -> str:
        if self._connection_status:
            return "Connection status: online"
        else:
            return "Connection status: offline"


con_params1 = {"$servername": "127.0.0.1",
              "$username": "Kownak",
              "$password": "1234"}

con_params2 = {"$servername": "1.0.0.127",
              "$username": "vas",
              "$password": "444"}

db1 = DatabaseConnection(con_params1)
print(db1.check_status())
print(db1.connect())

db2 = DatabaseConnection(con_params2)
print(db2.check_status())
print(db2.connect())
print(db2.disconnect())
print(db2.connect())
