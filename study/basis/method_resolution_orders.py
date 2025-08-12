class Base:
    def __init__(self):
        print("Base init")

class X(Base):
    def __init__(self):
        print("X init")
        super().__init__()

class Y(Base):
    def __init__(self):
        print("Y init")
        super().__init__()

class Z(Base):
    def __init__(self):
        print("Z init")
        super().__init__()

class A(X, Y):
    def __init__(self):
        print("A init")
        super().__init__()

class B(Y, X):
    def __init__(self):
        print("B init")
        super().__init__()

class C(X, Z):
    def __init__(self):
        print("C init")
        super().__init__()

class D(A, C):
    def __init__(self):
        print("D init")
        super().__init__()

# TypeError: Cannot create a consistent method resolution order (MRO) for bases X, Y. Because X precedes Y in the MRO of A, but Y precedes X in the MRO of B.
# class C(A, B):
#     def __init__(self):
#         print("C init")
#         super().__init__()

if __name__ == "__main__":
    print("Creating instance of A:")
    a = A()
    print("\nCreating instance of B:")
    b = B()
    print("\nCreating instance of D:")
    d = D()

    print("\nMethod Resolution Order for A:", A.__mro__)
    print("Method Resolution Order for B:", B.__mro__)
    print("Method Resolution Order for D:", D.__mro__)