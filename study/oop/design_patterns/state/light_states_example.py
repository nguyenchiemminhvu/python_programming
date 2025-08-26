from abc import ABC, abstractmethod

class context(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def get_current_state(self):
        pass
    
    @abstractmethod
    def set_current_state(self, state):
        pass

class light_state(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def on_enter(self, context):
        pass
    
    @abstractmethod
    def on_toggle(self, context):
        pass
    
    @abstractmethod
    def on_exit(self, context):
        pass

class light_state_off(light_state):
    def __init__(self):
        super().__init__()

    def on_enter(self, context):
        print("Light is turned OFF")

    def on_toggle(self, context):
        print("Switching light LOW...")
        self.on_exit(context)
        context.set_current_state(light_state_low())
        context.get_current_state().on_enter(context)

    def on_exit(self, context):
        print("Exiting OFF state")

class light_state_low(light_state):
    def __init__(self):
        super().__init__()

    def on_enter(self, context):
        print("Light is turned LOW")

    def on_toggle(self, context):
        print("Switching light HIGH...")
        self.on_exit(context)
        context.set_current_state(light_state_high())
        context.get_current_state().on_enter(context)

    def on_exit(self, context):
        print("Exiting LOW state")

class light_state_high(light_state):
    def __init__(self):
        super().__init__()

    def on_enter(self, context):
        print("Light is turned HIGH")

    def on_toggle(self, context):
        print("Switching light OFF...")
        self.on_exit(context)
        context.set_current_state(light_state_off())
        context.get_current_state().on_enter(context)

    def on_exit(self, context):
        print("Exiting HIGH state")

class light(context):
    def __init__(self):
        super().__init__()
        self._cur_state = light_state_off()

    def get_current_state(self):
        return self._cur_state
    
    def set_current_state(self, state):
        self._cur_state = state
    
    def toggle(self):
        self._cur_state.on_toggle(self)

if __name__ == "__main__":
    light_obj = light()
    light_obj.get_current_state().on_enter(light_obj)

    while True:
        command = input("Press 't' to toggle the light state or 'q' to quit: ")
        if command.lower() == 't':
            light_obj.toggle()
        elif command.lower() == 'q':
            break
        else:
            print("Invalid command. Please try again.")