from abc import ABC, abstractmethod
from multipledispatch import dispatch

class visitor(ABC):
    def __init__(self):
        pass

class graphic_item(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass

    @abstractmethod
    def draw(self):
        pass

class circle(graphic_item):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def accept(self, visitor):
        return visitor.export(self)

    def draw(self):
        return f"Drawing a circle with radius {self.radius}"

class square(graphic_item):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def accept(self, visitor):
        return visitor.export(self)

    def draw(self):
        return f"Drawing a square with side {self.side}"

class export_visitor(visitor):
    def __init__(self):
        super().__init__()

    @dispatch(graphic_item)
    def export(self, item):
        return f"Exporting {item}"

    @dispatch(circle)
    def export(self, c):
        return f"Exporting circle with radius {c.radius}"

    @dispatch(square)
    def export(self, s):
        return f"Exporting square with side {s.side}"

if __name__ == "__main__":
    circle_item = circle(5)
    square_item = square(4)

    export = export_visitor()
    
    print(circle_item.draw())
    print(circle_item.accept(export))

    print(square_item.draw())
    print(square_item.accept(export))