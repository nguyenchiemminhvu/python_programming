from abc import ABC, abstractmethod

class Button(ABC):
    def __init__(self, label):
        self.label = label

    @abstractmethod
    def click(self):
        raise NotImplementedError("Subclasses should implement this method.")
    
    @abstractmethod
    def render(self):
        raise NotImplementedError("Subclasses should implement this method.")

class WindowsButton(Button):
    def click(self):
        print(f"Windows Button '{self.label}' clicked.")

    def render(self):
        print(f"Rendering Windows Button with label: {self.label}")

class LinuxButton(Button):
    def click(self):
        print(f"Linux Button '{self.label}' clicked.")

    def render(self):
        print(f"Rendering Linux Button with label: {self.label}")

class Dialog(ABC):
    @abstractmethod
    def create_button(self):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def render(self):
        button = self.create_button()
        button.render()
        print("Dialog rendered.")

class WindowsDialog(Dialog):
    def create_button(self):
        return WindowsButton("OK")

class LinuxDialog(Dialog):
    def create_button(self):
        return LinuxButton("OK")

class Application:
    def __init__(self, dialog: Dialog):
        self.dialog = dialog

    def run(self):
        self.dialog.render()

if __name__ == "__main__":
    config = input("Choose OS (windows/linux): ").strip().lower()
    dialog = None
    if config == "windows":
        dialog = WindowsDialog()
    elif config == "linux":
        dialog = LinuxDialog()
    else:
        raise ValueError("Unsupported OS type.")
    
    app = Application(dialog)
    app.run()