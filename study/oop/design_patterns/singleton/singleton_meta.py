class Singleton(type):
    __instance = None
    
    def __call__(self, *args, **kwds):
        if not self.__instance:
            self.__instance = super().__call__(*args, **kwds)
        return self.__instance

class SingletonClass(metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.value = 42

if __name__ == "__main__":
    s1 = SingletonClass()
    s2 = SingletonClass()
    print(s1 is s2)
    s1.value = 100
    print(s2.value)