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

class SingletonChild2(Singleton):
    def __init__(self):
        super().__init__()
        self.another_property = "I am a property of SingletonChild2"

if __name__ == "__main__":
    s1 = SingletonChild()
    s2 = SingletonChild()
    print(s1 is s2)  # Should print True, proving both are the same instance
    s1.some_property = "Changed property"
    print(s2.some_property)
    
    s3 = SingletonChild2()
    s4 = SingletonChild2()
    print(s3 is s4)  # Should print True, proving both are the same instance
    s4.another_property = "Changed property"
    print(s3.another_property)
    
    print(s1 is s3)  # Should print False, proving they are different singleton instances