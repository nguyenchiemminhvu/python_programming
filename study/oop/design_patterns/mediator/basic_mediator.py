from abc import ABC, abstractmethod

class mediator(ABC):
    @abstractmethod
    def notify(self, sender: str, event: str) -> None:
        """Notify the mediator of an event."""
        pass

class component(ABC):
    def __init__(self, m: mediator) -> None:
        self._mediator = m

class clickable(ABC):
    @abstractmethod
    def click(self) -> None:
        pass

class checkable(ABC):
    @abstractmethod
    def check(self) -> None:
        pass

class gui_item(component):
    def __init__(self, m: mediator, name: str) -> None:
        super().__init__(m)
        self.name = name

    def set_text(self, text: str) -> None:
        print(f"{self.name} set to '{text}'")
        self._mediator.notify(self.name, "set_text")

class button(gui_item, clickable):
    def __init__(self, m: mediator, name: str) -> None:
        super().__init__(m, name)

    def click(self) -> None:
        print(f"Button {self.name} clicked")
        self._mediator.notify(self.name, "click")

class text_box(gui_item):
    def __init__(self, m: mediator, name: str) -> None:
        super().__init__(m, name)

class check_box(gui_item, checkable):
    def __init__(self, m: mediator, name: str) -> None:
        super().__init__(m, name)

    def check(self) -> None:
        print(f"CheckBox {self.name} checked")
        self._mediator.notify(self.name, "check")

class dialog(mediator, gui_item):
    def __init__(self) -> None:
        self.button_ok = button(self, "OK")
        self.button_cancel = button(self, "Cancel")
        self.text_input = text_box(self, "Input")
        self.check_box = check_box(self, "Agree")
        self._items = {
            "OK": self.button_ok,
            "Cancel": self.button_cancel,
            "Input": self.text_input,
            "Agree": self.check_box
        }

    def notify(self, sender: str, event: str) -> None:
        print(f"Dialog notified by {sender} of event '{event}'")
        if event == "click":
            if sender == "OK":
                self.handle_ok()
            elif sender == "Cancel":
                self.handle_cancel()
            elif sender == "Agree":
                self.handle_agree()
        elif event == "set_text":
            print(f"Text input changed: {self.text_input.name}")
        else:
            print(f"Unhandled event '{event}' from {sender}")
    
    def handle_ok(self) -> None:
        print("OK button pressed. Processing input...")
        input_text = self.text_input.name
        print(f"Input text: {input_text}")
        if self.check_box.name == "Agree":
            print("Checkbox is checked. Proceeding with action.")
        else:
            print("Checkbox is not checked. Action cancelled.")
    
    def handle_cancel(self) -> None:
        print("Cancel button pressed. Closing dialog without action.")
    
    def handle_agree(self) -> None:
        print("Checkbox checked. Ready to proceed with action.")
        self.check_box.check()

if __name__ == "__main__":
    dialog_instance = dialog()
    dialog_instance.text_input.set_text("Sample input")
    dialog_instance.button_ok.click()
    dialog_instance.check_box.check()
    dialog_instance.button_cancel.click()
    dialog_instance.button_ok.set_text("Confirm")
    dialog_instance.button_ok.click()