from abc import ABC, abstractmethod


class AbstractDocument(ABC):
    size: int
    content: list

    def __init__(self, size: int, content: list) -> None:
        self.size = size
        self.content = content

    @abstractmethod
    def get_content(self) -> str:
        pass


class DocumentPDF(AbstractDocument):
    size: int

    def get_content(self) -> str:
        return " ".join(self.content)


class Renderer(ABC):
    document: AbstractDocument

    def __init__(self, document: AbstractDocument) -> None:
        self.document = document

    @abstractmethod
    def render_document(self) -> str:
        pass


class LightThemeRenderer(Renderer):
    document: AbstractDocument

    def render_document(self) -> str:
        return "(Light) " + self.document.get_content() + " (Light)"


class DarkThemeRenderer(Renderer):
    document: AbstractDocument

    def render_document(self) -> str:
        return "(Dark) " + self.document.get_content() + " (Dark)"


pdf1 = DocumentPDF(1024, ["Tu", "jest", "tekst"])


render_light = LightThemeRenderer(pdf1)
print(render_light.render_document())

render_dark = DarkThemeRenderer(pdf1)
print(render_dark.render_document())
