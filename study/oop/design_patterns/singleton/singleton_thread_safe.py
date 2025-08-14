import threading

class Singleton:
    __instance = None
    __lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        pass

class SingletonClass(Singleton):
    def __init__(self):
        super().__init__()
        self.value = 0

if __name__ == "__main__":
    s1 = SingletonClass()
    s2 = SingletonClass()
    print(s1 is s2)  # True
    s1.value = 42
    print(s2.value)