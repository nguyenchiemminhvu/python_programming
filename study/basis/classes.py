class Sample:
    a = 0
    b = 0
    c = 0

s1 = Sample()
print(s1.a, s1.b, s1.c)  # Output: 0 0 0
s1.a = 1
print(s1.a, s1.b, s1.c)  # Output: 1 0 0

class SampleInit:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

s1 = SampleInit()
print(s1.a, s1.b, s1.c)  # Output: 0 0 0
s1.a = 1
print(s1.a, s1.b, s1.c)  # Output: 1 0 0

class SampleStr:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
    
    def __str__(self):
        return f"a: {self.a}, b: {self.b}, c: {self.c}"

s1 = SampleStr()
print(s1)  # Output: a: 0, b: 0, c: 0
s1.a = 1
print(s1)  # Output: a: 1, b: 0, c: 0

class SampleMethods:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def display(self):
        print(f"a: {self.a}, b: {self.b}, c: {self.c}")
    
    def cleanup(self):
        del self.a
        del self.b
        del self.c

s1 = SampleMethods()
s1.display()  # Output: a: 0, b: 0, c: 0
s1.a = 1
s1.display()  # Output: a: 1, b: 0, c: 0
s1.cleanup()
try:
    s1.display()  # Raises AttributeError since a, b, c are deleted
except AttributeError as e:
    print(e)
