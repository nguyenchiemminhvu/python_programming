# Equality and hashability

class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

# Example usage
person1 = Person("Alice")
person2 = Person("Alice")
person3 = Person("Bob")
print(person1 == person2)  # True, same name
print(person1 == person3)  # False, different name
print(hash(person1))  # Hash based on name
print(hash(person2))  # Same hash as person1
print(hash(person3))  # Different hash

