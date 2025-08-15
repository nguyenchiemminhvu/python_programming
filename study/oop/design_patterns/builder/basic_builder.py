from abc import ABC, abstractmethod

class i_builder(ABC):
    @abstractmethod
    def reset(self):
        raise NotImplementedError("This method should be overridden by subclasses.")
    
    @abstractmethod
    def build_part_a(self):
        raise NotImplementedError("This method should be overridden by subclasses.")
    
    @abstractmethod
    def build_part_b(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

class ConcreteBuilderA(i_builder):
    def __init__(self):
        self.product = []
    
    def reset(self):
        self.product = []
    
    def build_part_a(self):
        self.product.append("Part A")
    
    def build_part_b(self):
        self.product.append("Part B")

class ConcreteBuilderB(i_builder):
    def __init__(self):
        self.product = []
    
    def reset(self):
        self.product = []
    
    def build_part_a(self):
        self.product.append("Part A")
    
    def build_part_b(self):
        self.product.append("Part B")

class Director:
    def __init__(self, builder: i_builder):
        self.builder = builder
    
    def construct(self):
        self.builder.reset()
        self.builder.build_part_a()
        self.builder.build_part_b()
        return self.builder.product

if __name__ == "__main__":
    config = input("Choose builder (A/B): ").strip().upper()
    builder = None
    if config == 'A':
        builder = ConcreteBuilderA()
    elif config == 'B':
        builder = ConcreteBuilderB()
    else:
        raise ValueError("Invalid builder choice. Choose either A or B.")
    
    director = Director(builder)
    product = director.construct()
    print("Constructed product:", product)