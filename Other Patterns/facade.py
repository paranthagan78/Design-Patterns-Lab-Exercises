"""
The Facade pattern is a way to provide a simpler unified interface to
a more complex system. It provides an easier way to access functions
of the underlying system by providing a single entry point.
This pattern can be seen in the Python standard library.
"""
class CPU:

    def freeze(self):
        print("Freezing processor.")

    def jump(self, position):
        print("Jumping to:", position)

    def execute(self):
        print("Executing.")


class Memory:
    
    def load(self, position, data):
        print(f"Loading from {position} data: '{data}'.")


class SolidStateDrive:
    
    def read(self, lba, size):
        print(f"Some data from sector {lba} with size {size}")


class ComputerFacade:
    
    def __init__(self):
        #self.name=name
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00","Hai This is my World")
        self.cpu.jump("0x00")
        self.cpu.execute()
        self.ssd.read("0x1000","100k")

#driver code
        
computer_facade = ComputerFacade()
computer_facade.start()