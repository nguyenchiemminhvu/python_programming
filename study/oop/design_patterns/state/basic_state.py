from abc import ABC, abstractmethod
import time

class context(ABC):
    @abstractmethod
    def change_state(self, s : "state"):
        pass

class state(ABC):
    @abstractmethod
    def operating(self, c : context):
        pass

class concrete_state_A(state):
    def operating(self, c: context):
        print("State A is operating.")

class concrete_state_B(state):
    def operating(self, c: context):
        print("State B is operating.")

class concrete_context(context):
    def __init__(self):
        self.state = None
    
    def change_state(self, s: state):
        self.state = s
    
    def operate(self):
        if self.state is not None:
            self.state.operating(self)
    
if __name__ == "__main__":
    c = concrete_context()
    c.change_state(concrete_state_A())
    c.operate()
    time.sleep(1)
    c.change_state(concrete_state_B())
    c.operate()
    c.operate()