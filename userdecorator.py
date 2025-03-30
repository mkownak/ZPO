from abc import ABC, abstractmethod
from typing import Any

class User(ABC):
    @abstractmethod
    def get_permissions(self) -> list:
        pass

class BaseUser(User):
    def get_permissions(self) -> list:
        return ["read", "write"]

class Decorator(ABC):
    def __init__(self, obj: Any) -> None:
        self.obj = obj

    @abstractmethod
    def get_permissions(self) -> list:
        pass


class GuestDecorator(Decorator):
    def get_permissions(self) -> list:
        prem = self.obj.get_permissions()
        prem.remove("write")
        return prem


class AdminDecorator(Decorator):
    def get_permissions(self) -> list:
        prem = self.obj.get_permissions()
        prem.append("remove")
        return prem

user1 = BaseUser()
print(user1.get_permissions())
guest = GuestDecorator(user1)
print(guest.get_permissions())
admin = AdminDecorator(user1)
print(admin.get_permissions())
