from abc import ABC, abstractmethod

class strategy_data:
    def __init__(self):
        pass

class strategy(ABC):
    @abstractmethod
    def execute(self, data: strategy_data) -> None:
        raise NotImplementedError("Subclasses must implement this method")

class concrete_strategy_a(strategy):
    def execute(self, data: strategy_data) -> None:
        print("Executing Concrete Strategy A")
        data.result = "Result from Concrete Strategy A"

class concrete_strategy_b(strategy):
    def execute(self, data: strategy_data) -> None:
        print("Executing Concrete Strategy B")
        data.result = "Result from Concrete Strategy B"

class context:
    def __init__(self, strategy: strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: strategy) -> None:
        self._strategy = strategy

    def execute_strategy(self, data: strategy_data) -> None:
        print("Context: Executing strategy")
        self._strategy.execute(data)
        print(f"Context: Result is {data.result}")

if __name__ == "__main__":
    data = strategy_data()
    context_instance = context(concrete_strategy_a())
    context_instance.execute_strategy(data)
    context_instance.set_strategy(concrete_strategy_b())
    context_instance.execute_strategy(data)