from abc import ABC, abstractmethod
import threading
import time
from typing import List, Dict
from collections import defaultdict

# enum event id here
class event_id:
    EVENT_KEYBOARD = 1
    EVENT_ON_EXIT = 2

class event_object(ABC):
    def __init__(self):
        pass

class event_listener(ABC):
    @abstractmethod
    def on_event(self, eid : int, obj: event_object):
        raise NotImplementedError("This method should be overridden by subclasses")

class keyboard_event_listener(event_listener):
    def on_event(self, eid : int, obj: event_object):
        if eid == event_id.EVENT_KEYBOARD:
            print(f"Keyboard Event: {obj.key}")

class on_exit_event_listener(event_listener):
    def on_event(self, eid : int, obj: event_object):
        if eid == event_id.EVENT_ON_EXIT:
            print(f"Exit Event: {obj.message}")

class event_manager(ABC):
    def __init__(self):
        self._listeners : Dict[int, List[listener]] = {}

    def subscribe(self, listener: event_listener, eid: int):
        if eid not in self._listeners:
            self._listeners[eid] = []
        self._listeners[eid].append(listener)

    def unsubscribe(self, listener: event_listener):
        for eid in self._listeners:
            if listener in self._listeners[eid]:
                self._listeners[eid].remove(listener)
                if not self._listeners[eid]:
                    del self._listeners[eid]

    def notify(self, eid: int, obj: event_object):
        for listener in self._listeners[eid]:
            listener.on_event(eid, obj)

class application(event_manager):
    def __init__(self):
        super().__init__()
        self.worker_thread = threading.Thread(target=self._run)
        self.worker_thread.start()
    
    def _run(self):
        while True:
            s = input("Typing something (type 'exit' to quit): ")
            if s.lower() == 'exit':
                exit_event = event_object()
                exit_event.message = "Application is exiting"
                self.notify(event_id.EVENT_ON_EXIT, exit_event)
                break

            for ch in s:
                key_event = event_object()
                key_event.key = ch
                self.notify(event_id.EVENT_KEYBOARD, key_event)

if __name__ == "__main__":
    app = application()

    keyboard_listener = keyboard_event_listener()
    exit_listener = on_exit_event_listener()
    app.subscribe(keyboard_listener, event_id.EVENT_KEYBOARD)
    app.subscribe(exit_listener, event_id.EVENT_ON_EXIT)

    print("Application started. Type something to see keyboard events.")
    print("Type 'exit' to quit the application.")
    app.worker_thread.join()