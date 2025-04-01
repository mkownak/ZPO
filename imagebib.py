from typing import Any


class Image:
    name: str
    size: int
    x: int
    y: int
    extension: str

    def __init__(self, name: str, size: int, x: int, y: int, extension: str) -> None:
        self.name = name
        self.size = size
        self.x = x
        self.y = y
        self.extension = extension
