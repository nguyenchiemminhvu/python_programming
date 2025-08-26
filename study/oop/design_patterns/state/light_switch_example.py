from abc import ABC, abstractmethod

class state(ABC):
    @abstractmethod
    def press(self, switch):
        pass

class OnState(state):
    def press(self, switch):
        print("Turning off the light.")
        switch.state = OffState()

class OffState(state):
    def press(self, switch):
        print("Turning on the light.")
        switch.state = OnState()

class LightSwitch:
    def __init__(self):
        self.state = OffState()

    def press(self):
        self.state.press(self)

if __name__ == "__main__":
    light_switch = LightSwitch()
    
    while (True):
        command = input("Press 't' to toggle the light switch or 'q' to quit: ")
        if command.lower() == 't':
            light_switch.press()
        elif command.lower() == 'q':
            break
        else:
            print("Invalid command. Please try again.")