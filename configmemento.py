import copy
class Memento:
    _states: list
    _i: int

    def __init__(self) -> None:
        self._states = []
        self._i = -1

    def save_state(self, state: str) -> None:
        if self._i != len(self._states) - 1:
            self._states = self._states[:self._i + 1]

        self._states.append(state)
        self._i += 1

    def undo(self) -> None:
        if self._i > 0:
            self._i -= 1

    def redo(self) -> None:
        if self._i < len(self._states) - 1:
            self._i += 1

    def read_state(self) -> str:
        return self._states[self._i]

    def read_states(self):
        return self._states


class App:
    def __init__(self) -> None:
        self.config = {"resolution": "800x600",
                        "DPI": 100}
        self.memento = Memento()
        self.memento.save_state(copy.copy(self.config))

    def change_resolution(self, res):
        self.config["resolution"] = res
        self.memento.save_state(copy.copy(self.config))

    def change_dpi(self, dpi):
        self.config["DPI"] = dpi
        self.memento.save_state(copy.copy(self.config))

    def show_config(self):
        return self.memento.read_state()

    def undo(self):
        self.memento.undo()
        self.config = self.memento.read_state()

    def redo(self) -> None:
        self.memento.redo()
        self.config = self.memento.read_state()

    def show_all(self):
        return self.memento.read_states()


appka = App()
print(appka.show_config())
appka.change_resolution("1920x1020")
print(appka.show_config())
appka.undo()
print(appka.show_config())
