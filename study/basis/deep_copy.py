import copy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def clone(self):
        return copy.deepcopy(self)

if __name__ == "__main__":
    p1 = Person("Alice", 30)
    p2 = p1.clone()
    print(f"Original: {p1.name}, {p1.age}")
    print(f"Clone: {p2.name}, {p2.age}")
    print(p1 is p2)  # Should print False, since p2 is a deep copy