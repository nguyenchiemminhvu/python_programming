# python 3.11.5+

from typing import Generic, TypeVar, List

# Define a TypeVar to represent the generic type
T = TypeVar("T")

class Stack(Generic[T]):
    """
    A generic Stack implementation that can hold elements of any specified type.
    """
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """Adds an item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> T:
        """Removes and returns the item from the top of the stack."""
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T | None:
        """Returns the item at the top of the stack without removing it."""
        if not self._items:
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        """Checks if the stack is empty."""
        return len(self._items) == 0

# Usage examples
if __name__ == "__main__":
    # Stack of integers
    int_stack = Stack[int]()
    int_stack.push(10)
    int_stack.push(20)
    print(f"Integer stack peek: {int_stack.peek()}")
    print(f"Popped from integer stack: {int_stack.pop()}")
    print(f"Integer stack empty: {int_stack.is_empty()}")

    # Stack of strings
    str_stack = Stack[str]()
    str_stack.push("hello")
    str_stack.push("world")
    print(f"String stack peek: {str_stack.peek()}")
    print(f"Popped from string stack: {str_stack.pop()}")
    print(f"String stack empty: {str_stack.is_empty()}")