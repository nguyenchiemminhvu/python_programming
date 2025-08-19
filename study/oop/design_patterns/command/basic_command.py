from abc import ABC, abstractmethod
import time

class singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

class receiver:
    def __init__(self):
        pass

class clipboard(singleton, receiver):
    def __init__(self):
        super().__init__()
        self._text_arr = []
    
    def add_text(self, text):
        print(f"Adding text to clipboard: {text}")
        self._text_arr.append(text)
    
    def get_text(self):
        print("Retrieving text from clipboard")
        text = self._text_arr.pop() if self._text_arr else None
        return text

    def clear(self):
        print("Clearing clipboard")
        self._text_arr.clear()

clipboard_instance = clipboard()

class command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError("Subclasses must implement the execute method")

class copy_command(command):
    def __init__(self, rec : receiver, text:str):
        self._text = text
        self._receiver = rec

    def execute(self):
        print("copy_command executed")
        self._receiver.add_text(self._text)

class paste_command(command):
    def __init__(self, rec: receiver):
        self._receiver = rec

    def execute(self):
        print("paste_command executed")
        text = self._receiver.get_text()
        if text:
            print(f"Pasted text: {text}")
        else:
            print("No text to paste")

class clear_clipboard_command(command):
    def __init__(self, rec: receiver):
        self._receiver = rec

    def execute(self):
        print("clear_clipboard_command executed")
        self._receiver.clear()

class invoker:
    def __init__(self):
        self._commands = []
    
    def add_command(self, cmd: command):
        self._commands.append(cmd)
    
    def execute_commands(self):
        for cmd in self._commands:
            cmd.execute()

if __name__ == "__main__":
    # client code
    inv = invoker()
    
    while (True):
        try:
            text = input("Enter text to copy: ")
            if (text.lower() == 'exit'):
                break
            inv.add_command(copy_command(clipboard_instance, text))
            inv.add_command(paste_command(clipboard_instance))
        except KeyboardInterrupt:
            print()
            inv.add_command(clear_clipboard_command(clipboard_instance))
            break
        finally:
            inv.execute_commands()