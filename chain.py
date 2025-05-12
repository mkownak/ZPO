from abc import ABC

class Application:
    text: str
    level: int

    def __init__(self, text:str, level:int) -> None:
        self.text = text
        self.level = level

class Member(ABC):
    task: str

    def process(self, app) -> bool | None:
        print(f"This application level {app.level} is not part of my job")


class CEO(Member):
    def process(self, app) -> bool | None:
        if app.level == 1:
            print("App aproved by CEO")
            return True
        else:
            return False


class CTO(Member):
    def process(self, app) -> bool | None:
        if app.level == 2:
            print("App aproved by CTO")
            return True
        else:
            return False

class TTO(Member):
    def process(self, app) -> bool | None:
        if app.level == 3:
            print("App aproved by TTO")
            return True
        else:
            return False


class Chain:
    chain: list

    def __init__(self):
        self.chain = []

    def run_task(self, task) -> None:
        for link in self.chain:
            result = link.process(task)
            if result:
                break

app = Application("cos tam", level=2)

chain = Chain()

chain.chain.append(CEO())
chain.chain.append(CTO())
chain.chain.append(TTO())

chain.run_task(app)
