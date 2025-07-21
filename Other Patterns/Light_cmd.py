# Command Interface
class Command:
    def execute(self):
        pass
    
# Concrete Command
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

# Receiver
class Light:
    def turn_on(self):
        print("Light is ON")

# Invoker
class RemoteControl:
    def __init__(self): 
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Client Code
if __name__ == "__main__":
    # Creating objects
    light = Light()
    light_on = LightOnCommand(light)

    remote = RemoteControl()

    # Setting the command
    remote.set_command(light_on)

    # Pressing the button
    remote.press_button()


"""
# Command Interface
class Command:
    def execute(self):
        pass
    
# Concrete Command
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        com=input("Enter Command (ON/OFF): ")

        if com=="ON":
            self.light.turn_on()
        elif com=="OFF":
            self.light.turn_off()

# Receiver
class Light:
    def turn_on(self):
        print("Light is ON")
    
    def turn_off(self):
        print("Light is OFF")

# Invoker
class RemoteControl:
    def __init__(self): 
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Client Code
# Creating objects
light = Light()
light_on = LightOnCommand(light)
remote = RemoteControl()
# Setting the command
remote.set_command(light_on)
# Pressing the button
remote.press_button()
"""