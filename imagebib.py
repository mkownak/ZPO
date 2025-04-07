from typing import Any


class Image:
    name: str
    size: int
    x: int
    y: int
    extension: str
    rgb_values: dict

    def __init__(self, name: str, size: int, x: int, y: int, extension: str, rgb_values:dict) -> None:
        self.name = name
        self.size = size
        self.x = x
        self.y = y
        self.extension = extension
        self.rgb_values = rgb_values

    def __str__(self) -> str:
        return f"{self.name}.{self.extension}, {self.x}x{self.y}px, {self.size}KB"


class ImageScaler:
    def scale(self, image: Image, factor: float) -> None:
        image.x = int(image.x * factor)
        image.y = int(image.y * factor)
        print(f"Przeskalowano do: {image.x}x{image.y}px")


class ImageColorChanger:
    def change_color(self, image: Image, color_key:str, value:int) -> None:
        image.rgb_values[color_key] = value
        print(f"Zmieniono wartość koloru {color_key} na: {value}")


class ImageCompressor:
    def compress(self, image: Image, ratio: float) -> None:
        original = image.size
        image.size = int(image.size * ratio)
        print(f"Skompresowano: {original}KB do {image.size}KB")


class ImageFacade:
    def __init__(self) -> None:
        self.scaler = ImageScaler()
        self.color_changer = ImageColorChanger()
        self.compressor = ImageCompressor()

    def scale_image(self, image: Image, scale: float) -> None:
        self.scaler.scale(image, scale)

    def change_colors(self, image: Image, color_updates: dict) -> None:
        for color, value in color_updates.items():
            self.color_changer.change_color(image, color, value)

    def compress_image(self, image: Image, ratio: float) -> None:
        self.compressor.compress(image, ratio)

    def process_image(self, image: Image, scale: float, color_updates: dict, compress_ratio: float) -> None:
        self.scale_image(image, scale)
        self.change_colors(image, color_updates)
        self.compress_image(image, compress_ratio)



image = Image("lena", 4096, 1024, 800, "jpg", {"R": 100, "G": 100, "B": 100})
facade = ImageFacade()

facade.scale_image(image, 2)

print(image)
