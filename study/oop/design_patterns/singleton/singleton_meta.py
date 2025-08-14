class Singleton(type):
    __instance = None
    
    def __call__(cls, *args, **kwds):
        if not cls.__instance:
            cls.__instance = super().__call__(*args, **kwds) # call the type.__new__ and __init__
        return cls.__instance

class SingletonClass(metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.value = 42

class SingletonClass2(metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.another_value = 84

if __name__ == "__main__":
    s1 = SingletonClass()
    s2 = SingletonClass()
    print(s1 is s2)
    s1.value = 100
    print(s2.value)
    
    s3 = SingletonClass2()
    s4 = SingletonClass2()
    print(s3 is s4)
    s4.another_value = 200
    print(s3.another_value)
    
    print(s1 is s3)  # Should be False, different singleton classes