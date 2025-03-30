class Oldprinter:
    def print_old(self)->str:
        return "Old Printer"


class PrinterAdapter:
    def __init__(self, Oldprinter: Oldprinter):
        self.printer = Oldprinter

    def print_new(self)->str:
        old_string = self.printer.print_old()
        new_string = "New" + old_string[3:]
        return new_string


old_p = Oldprinter()
adapter_p = PrinterAdapter(old_p)
print(adapter_p.print_new())
