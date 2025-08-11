class Shape():
    def __init__(self, name):
        self.name = name

    @property
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    @property
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    @property
    def area(self):
        return 3.14159 * self.radius ** 2
    
    @property
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

if __name__ == "__main__":
    circle = Circle(5)
    print(f"Shape: {circle.name}")
    print(f"Area: {circle.area}")
    print(f"Perimeter: {circle.perimeter}")

    circle.radius = 10
    print(f"Updated Radius: {circle.radius}")
    print(f"Updated Area: {circle.area}")
    print(f"Updated Perimeter: {circle.perimeter}")