class Computer:
    def __init__(self, motherboard:str, cpu:str, gpu:str, ram:str, storage:str)->None:
        self.motherboard = motherboard
        self.cpu = cpu
        self.gpu = gpu
        self.storage = storage
        self.ram = ram

    def __str__(self):
        return f"Komputer z {self.motherboard} płytą główną,{self.gpu} GPU, {self.cpu} CPU, {self.ram} GB RAM, {self.storage}GB dysk,"


class MotherboardBuilder:
    def __init__(self):
        self.motherboard = None
        self.cpu = None
        self.gpu = None

    def set_motherboard(self, motherboard:str)->None:
        self.motherboard = motherboard


    def set_cpu(self, cpu:str)->None:
        self.cpu = cpu


    def set_gpu(self, gpu:str)->None:
        self.gpu = gpu


    def build(self)->tuple:
        if self.motherboard is not None and self.cpu is not None and self.gpu is not None:
            return (self.motherboard, self.cpu, self.gpu)
        else:
            raise ValueError("brakuje komponentow")


class StorageBuilder:
    def __init__(self):
        self.ram = None
        self.storage = None

    def set_ram(self, ram):
        self.ram = ram


    def set_storage(self, storage):
        self.storage = storage


    def build(self)->tuple:
        if self.ram is not None and self.storage is not None:
            return (self.ram, self.storage)
        else:
            raise ValueError("brakuje komponentow")


class ComputerBuilder:
    def __init__(self):
        self.motherboard_builder = MotherboardBuilder()
        self.storage_builder = StorageBuilder()

    def set_motherboard(self, motherboard):
        self.motherboard_builder.set_motherboard(motherboard)


    def set_cpu(self, cpu):
        self.motherboard_builder.set_cpu(cpu)


    def set_gpu(self, gpu):
        self.motherboard_builder.set_gpu(gpu)


    def set_ram(self, ram):
        self.storage_builder.set_ram(ram)


    def set_storage(self, storage):
        self.storage_builder.set_storage(storage)


    def build(self):
        motherboard, cpu, gpu = self.motherboard_builder.build()
        ram, storage = self.storage_builder.build()
        if motherboard is not None and cpu is not None and gpu is not None:
            if ram is not None and storage is not None:
                return Computer(motherboard, cpu, gpu, ram, storage)

builder = ComputerBuilder()
builder.set_motherboard("ASUS ROG STRIX Z790")
builder.set_cpu("Intel i7")
builder.set_gpu("NVIDIA RTX 4060")
builder.set_ram("32")
builder.set_storage("1000")
computer = builder.build()
print(computer)