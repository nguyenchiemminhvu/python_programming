from abc import ABC, abstractmethod

class Color(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def fill(self):
        raise NotImplementedError("Subclasses must implement this method")

class Shape(ABC):
    def __init__(self):
        self.color = None

    def fill_color(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self):
        raise NotImplementedError("Subclasses must implement this method")

class Red(Color):
    def fill(self):
        return "Filling with red color"

class Blue(Color):
    def fill(self):
        return "Filling with blue color"

class Circle(Shape):
    def draw(self):
        return f"Drawing a circle with color: {self.color.fill()}"

class Square(Shape):
    def draw(self):
        return f"Drawing a square with color: {self.color.fill()}"

if __name__ == "__main__":
    red = Red()
    blue = Blue()

    circle = Circle()
    circle.fill_color(red)
    print(circle.draw())

    square = Square()
    square.fill_color(blue)
    print(square.draw())