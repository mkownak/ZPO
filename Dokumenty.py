from abc import ABC, abstractmethod

class Document(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def write(self, line:str):
        pass

class WorldDocument(Document):
    def open(self)->str:
        return "Opening World"

    def write(self, line:str) -> str:
        return f"Writing {line} to World"


class PDFDocument(Document):
    def open(self) -> str:
        return "Opening PDF"

    def write(self, line: str) -> str:
        return f"Writing {line} to PDF"

class DocumentFactory:

    @staticmethod
    def create_document(file_name:str) -> Document:
        if file_name.endswith(".docx"):
            return WorldDocument()
        elif file_name.endswith(".pdf"):
            return PDFDocument()
        else:
            raise ValueError("Unsupported file type")

doc1 = DocumentFactory.create_document("test.docx")
doc2 = DocumentFactory.create_document("test2.pdf")

print(doc1.open())
print(doc2.open())


