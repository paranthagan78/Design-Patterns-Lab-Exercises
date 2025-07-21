from abc import ABC, abstractmethod

# State interface
class TrafficSignalState(ABC):
    @abstractmethod
    def change_signal(self):
        pass

# Concrete states
class RedState(TrafficSignalState):
    def change_signal(self):
        print("Traffic signal is red. Changing to yellow.")
        return YellowState()

class YellowState(TrafficSignalState):
    def change_signal(self):
        print("Traffic signal is yellow. Changing to green.")
        return GreenState()

class GreenState(TrafficSignalState):
    def change_signal(self):
        print("Traffic signal is green. Changing to red.")
        return RedState()


# Context class
class TrafficSignalController:
    def __init__(self):
        self.state = RedState()

    def get_state(self):
        return type(self.state).__name__

    def change_signal(self):
        self.state = self.state.change_signal()

# Example usage
traffic_controller = TrafficSignalController()

# Change signal from red to yellow
traffic_controller.change_signal()
print("Current state:", traffic_controller.get_state())

# Change signal from yellow to green
traffic_controller.change_signal()
print("Current state:", traffic_controller.get_state())

# Change signal from green to red
traffic_controller.change_signal()
print("Current state:", traffic_controller.get_state())
