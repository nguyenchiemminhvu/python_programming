class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

if __name__ == "__main__":
    # Testing the Singleton class
    instance1 = Singleton()
    instance2 = Singleton()

    print(instance1 is instance2)  # Should print True, indicating both are the same instance
    print(id(instance1), id(instance2))  # Should print the same ID for both instances