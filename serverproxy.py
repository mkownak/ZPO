from abc import ABC, abstractmethod

class AbstractServer(ABC):
    db: list
    @abstractmethod
    def add(self, obj:str):
        pass

    @abstractmethod
    def retrieve_all(self):
        pass

    @abstractmethod
    def remove(self):
        pass

class Server(AbstractServer):
    db: list

    def __init__(self) -> None:
        self.db = []

    def add(self, obj: str):
        self.db.append(obj)
        print(f"{obj} added")

    def retrieve_all(self):
        return self.db

    def remove(self):
        self.db.pop()
        print("last element removed")

class User:
    name: str
    permissions: list

    def __init__(self, name: str, permissions: list):
        self.name = name
        self.permissions = permissions


class ProxyApi(AbstractServer):
    client: User
    server: Server

    def __init__(self, server: Server, client: User):
        self.server = server
        self.client = client

    def add(self, obj: str):
        if "add" in self.client.permissions:
            self.server.add(obj)
        else:
            print("no permission")

    def retrieve_all(self):
        if "retrieve" in self.client.permissions:
            return self.server.retrieve_all()
        else:
            print("no permission")

    def remove(self):
        if "remove" in self.client.permissions:
            self.server.remove()
        else:
            print("no permission")

uzytnik = User("uzytnik", ["add", "retrieve", "remove"])
s1 = Server()
proxy_s1 = ProxyApi(s1, uzytnik)
proxy_s1.add("eldo")
proxy_s1.add("odle")
print(proxy_s1.retrieve_all())
proxy_s1.remove()
print(proxy_s1.retrieve_all())
