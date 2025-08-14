class Singleton:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

class SingletonChild(Singleton):
    def __init__(self):
        super().__init__()
        self.some_property = "I am a property of SingletonChild"
    

if __name__ == "__main__":
    s1 = SingletonChild()
    s2 = SingletonChild()
    print(s1 is s2)  # Should print True, proving both are the same instance
    s1.some_property = "Changed property"
    print(s2.some_property)