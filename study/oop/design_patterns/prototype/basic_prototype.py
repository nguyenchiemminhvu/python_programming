from abc import ABC, abstractmethod
import copy

class prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class shape(prototype):
    __auto_id = 0
    def __init__(self, color):
        self.id = shape.__auto_id
        shape.__auto_id += 1
        self.color = color
    
    def clone(self):
        raise NotImplementedError("Subclasses must implement clone method")

class circle(shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def clone(self):
        return circle(self.color, self.radius)

class rectangle(shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def clone(self):
        return rectangle(self.color, self.width, self.height)

if __name__ == "__main__":
    shapes = {
        "circle1": circle("red", 5),
        "rectangle1": rectangle("blue", 10, 20)
    }
    
    cloned_shapes = []
    cloned_shapes.append(shapes["circle1"].clone())
    cloned_shapes.append(shapes["rectangle1"].clone())
    cloned_shapes.append(shapes["circle1"].clone())

    for shape in cloned_shapes:
        print(f"Cloned {shape.__class__.__name__} with ID {shape.id} and color {shape.color}")