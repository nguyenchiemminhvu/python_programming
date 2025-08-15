from abc import ABC, abstractmethod

class clickable(ABC):
    @abstractmethod
    def click(self):
        raise NotImplementedError("Subclasses should implement this method.")

class renderable(ABC):
    @abstractmethod
    def render(self):
        raise NotImplementedError("Subclasses should implement this method.")

class ui_item(renderable):
    def __init__(self, label):
        self.label = label

    @abstractmethod
    def render(self):
        raise NotImplementedError("Subclasses should implement this method.")

class button(ui_item, clickable):
    def click(self):
        print(f"Button '{self.label}' clicked.")

    @abstractmethod
    def render(self):
        raise NotImplementedError("Subclasses should implement this method.")

class label(ui_item):
    @abstractmethod
    def render(self):
        raise NotImplementedError("Subclasses should implement this method.")

class windows_button(button):
    def render(self):
        print(f"Rendering Windows Button with label: {self.label}")

class linux_button(button):
    def render(self):
        print(f"Rendering Linux Button with label: {self.label}")

class windows_label(label):
    def render(self):
        print(f"Rendering Windows Label with text: {self.label}")

class linux_label(label):
    def render(self):
        print(f"Rendering Linux Label with text: {self.label}")

class factory(ABC):
    @abstractmethod
    def create_button(self, label):
        raise NotImplementedError("Subclasses should implement this method.")

    @abstractmethod
    def create_label(self, text):
        raise NotImplementedError("Subclasses should implement this method.")

class windows_factory(factory):
    def create_button(self, label):
        return windows_button(label)

    def create_label(self, text):
        return windows_label(text)

class linux_factory(factory):
    def create_button(self, label):
        return linux_button(label)

    def create_label(self, text):
        return linux_label(text)

class application:
    def __init__(self, factory):
        self.factory = factory
    
    def run(self):
        button = self.factory.create_button("OK")
        label = self.factory.create_label("Hello, World!")
        
        button.render()
        button.click()
        label.render()

if __name__ == "__main__":
    config = input("OS (windows/linux): ").strip().lower()
    app = None
    if config == "windows":
        app = application(windows_factory())
    elif config == "linux":
        app = application(linux_factory())
    else:
        raise ValueError("Unsupported OS type. Please choose 'windows' or 'linux'.")
    
    app.run()