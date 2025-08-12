# duck typing theory: if it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.

class Duck:
    def __init__(self):
        self.sound = "Quack"
    
    def quack(self):
        return self.sound

class Dog:
    def __init__(self):
        self.sound = "Woof"
    
    def bark(self):
        return self.sound

class DuckToy(Duck):
    def __init__(self):
        super().__init__()
        self.sound = "Squeak"
    
def make_sound(duck):
    try:
        return duck.quack()
    except AttributeError:
        return "This object does not quack!"

if __name__ == "__main__":
    duck = Duck()
    dog = Dog()
    duck_toy = DuckToy()

    print(make_sound(duck))       # Output: Quack
    print(make_sound(dog))        # Output: This object does not quack!
    print(make_sound(duck_toy))   # Output: Squeak