from abc import ABC, abstractmethod

class component(ABC):
    @abstractmethod
    def operation(self) -> str:
        """Perform an operation."""
        pass

class leaf(component):
    @abstractmethod
    def operation(self) -> str:
        """Perform an operation for a leaf."""
        return "Leaf operation"

class composite(component):
    def __init__(self):
        self.children = []

    def add(self, child: component) -> None:
        """Add a child component."""
        self.children.append(child)

    def remove(self, child: component) -> None:
        """Remove a child component."""
        self.children.remove(child)

    @abstractmethod
    def operation(self) -> str:
        """Perform an operation for the composite."""
        results = [child.operation() for child in self.children]
        return "Composite operation with children: " + ", ".join(results)

class product(leaf):
    def operation(self) -> str:
        """Perform an operation for a product."""
        return "Product operation"

class box(composite):
    def operation(self) -> str:
        """Perform an operation for a box."""
        return "Box operation with children: " + super().operation()

if __name__ == "__main__":
    box1 = box()
    box1.add(product())
    box1.add(product())
    
    box2 = box()
    box2.add(product())
    box2.add(product())

    box1.add(box2)

    print(box1.operation())  # Output: Box operation with children: Product operation, Product operation, Box operation with children: Product operation, Product operation