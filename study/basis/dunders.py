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

# Orderability
class ComparablePerson:
    def __init__(self, name):
        self.name = name
    
    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name

# Example usage
person1 = ComparablePerson("Alice")
person2 = ComparablePerson("Bob")
print(person1 < person2)  # True
print(person1 == person2)  # False
print(person1 > person2)  # False

# Type conversion
class StringConverter:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"StringConverter({self.value!r})"

    def __int__(self):
        return int(round(float(self.value)))

    def __float__(self):
        return float(self.value)

# Example usage
converter = StringConverter("123.45")
print(str(converter))      # "123.45"
print(repr(converter))     # StringConverter('123.45')
print(int(converter))      # 123
print(float(converter))    # 123.45

# Callability
class CallableString:
    def __init__(self, value):
        self.value = value

    def __call__(self, times):
        return str(self.value) * times

# Example usage
callable_str = CallableString("Hello")
print(callable_str(3))  # "HelloHelloHello"

# Metaprogramming

class Meta(type):
    required_methods = [
        "do_something",
        "do_something_else"
    ]
    def __instancecheck__(self, instance):
        for method in self.required_methods:
            print(f"Checking method: {method} in {instance}")
            if not hasattr(instance, method):
                return False
        return True
    
    def __subclasscheck__(self, subclass):
        for method in self.required_methods:
            print(f"Checking method: {method} in {subclass}")
            if not hasattr(subclass, method):
                return False
        return True

# Example usage

class Base(metaclass=Meta):
    def do_something(self):
        pass

    def do_something_else(self):
        pass

class Derived(Base):
    def do_something(self):
        pass

    def do_something_else(self):
        pass

class NonDerived:
    def do_something(self):
        pass

# check instances and classes
print(isinstance(Derived(), Base))  # True
print(isinstance(NonDerived(), Base))  # True
print(issubclass(Derived, Base))  # True
print(issubclass(NonDerived, Base))  # True

# Attributes
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def __getattribute__(self, name):
        print(f"Accessing attribute: {name}")
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        if (name == "diameter"):
            return self.radius * 2
        elif (name == "area"):
            return 3.14 * (self.radius ** 2)
        else:
            print(f"Attribute {name} not found")
        return "default_value"
    
    def __setattr__(self, name, value):
        print(f"Setting attribute: {name} to {value}")
        super().__setattr__(name, value)

# Example usage
circle = Circle(5)
print(circle.radius)  # Accessing attribute: radius
print(circle.diameter)  # Accessing attribute: diameter
print(circle.area)  # Accessing attribute: area
print(circle.non_existent)  # Attribute non_existent not found, returning default value