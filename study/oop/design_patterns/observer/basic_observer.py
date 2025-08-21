from abc import ABC, abstractmethod
import threading
import time

class subject(ABC):
    def __init__(self):
        pass

class subscriber(ABC):
    @abstractmethod
    def on_notify(self, obj: subject):
        raise NotImplementedError("This method should be overridden by subclasses")

class concrete_subscriber(subscriber):
    def on_notify(self, obj: subject):
        print(f"Received update: {obj.message}")

class publisher(ABC):
    def __init__(self):
        self._subscribers = []

    def subscribe(self, s: subscriber):
        self._subscribers.append(s)

    def unsubscribe(self, s: subscriber):
        self._subscribers.remove(s)

class concrete_publishser(publisher):
    def __init__(self):
        super().__init__()
        self.checking_thread = threading.Thread(target=self._check_for_updates)
        self.checking_thread.daemon = True
        self.checking_thread.start()
    
    def _check_for_updates(self):
        while True:
            time.sleep(2)
            self.on_update("New update available!")
    
    def on_update(self, message: str):
        sub = subject()
        sub.message = message
        for s in self._subscribers:
            s.on_notify(sub)

if __name__ == "__main__":
    pub = concrete_publishser()
    
    sub1 = concrete_subscriber()
    sub2 = concrete_subscriber()
    
    pub.subscribe(sub1)
    pub.subscribe(sub2)
    
    quit = input("Press Enter to exit...\n")
    pub.unsubscribe(sub1)
    pub.unsubscribe(sub2)
