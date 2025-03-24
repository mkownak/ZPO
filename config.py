from abc import ABC, abstractmethod
from typing import Self
from copy import copy, deepcopy


class Prototype(ABC):
    @abstractmethod
    def deep_clone(self) -> Self:
        pass


class Config(Prototype):
    def __init__(self, fps_max:int, viewmodel:dict):
        self.fps_max = fps_max
        self.viewmodel = viewmodel

    def info(self):
        print(f"Max fps set to {self.fps_max}, viewmodel is: {self.viewmodel}")

    def deep_clone(self):
        return deepcopy(self)


viewmodel_pasha = {"viewmodel_offset_x": "2.5",
                   "viewmodel_offset_y": "2",
                   "viewmodel_offset_z": "-2",
                   "viewmodel_fov": "90"}

pasha_config = Config(400, viewmodel_pasha)
pasha_copy = pasha_config.deep_clone()

pasha_config.info()
pasha_copy.info()

pasha_copy.viewmodel["viewmodel_fov"] = "60"

pasha_config.info()
pasha_copy.info()
