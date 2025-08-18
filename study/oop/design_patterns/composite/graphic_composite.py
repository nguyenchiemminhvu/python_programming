from abc import ABC, abstractmethod

class i_positional():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

class graphical(ABC, i_positional):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    @abstractmethod
    def draw(self):
        raise NotImplementedError("Subclasses must implement this method")

class compound_graphical(graphical):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.children = []
    
    def add(self, child):
        if isinstance(child, graphical):
            self.children.append(child)
    
    def remove(self, child):
        if child in self.children:
            self.children.remove(child)
    
    def draw(self):
        for child in self.children:
            print(child.draw())

class dot(graphical):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def draw(self):
        return f"Drawing a dot at ({self.x}, {self.y})"

class line(graphical):
    def __init__(self, start_x, start_y, end_x, end_y):
        super().__init__(start_x, start_y)
        self.end_x = end_x
        self.end_y = end_y
    
    def draw(self):
        return f"Drawing a line from ({self.x}, {self.y}) to ({self.end_x}, {self.end_y})"

class circle(graphical):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    
    def draw(self):
        return f"Drawing a circle at ({self.x}, {self.y}) with radius {self.radius}"

if __name__ == "__main__":
    compound = compound_graphical()
    compound.add(dot(1, 2))
    compound.add(line(3, 4, 5, 6))
    compound.add(circle(7, 8, 10))

    sub_compound = compound_graphical()
    sub_compound.add(dot(9, 10))
    sub_compound.add(line(11, 12, 13, 14))
    compound.add(sub_compound)

    compound.draw()