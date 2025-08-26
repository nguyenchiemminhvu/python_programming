from typing import Callable

def execute_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    """
    Executes a given function with two integer arguments and returns the result.
    
    :param func: A callable that takes two integers and returns an integer.
    :param a: The first integer argument.
    :param b: The second integer argument.
    :return: The result of the function call.
    """
    return func(a, b)

# Example usage
if __name__ == "__main__":
    # Define a simple addition function
    def add(x: int, y: int) -> int:
        return x + y

    # Define a simple multiplication function
    def multiply(x: int, y: int) -> int:
        return x * y

    # Execute the functions using execute_function
    result_add = execute_function(add, 5, 3)
    result_multiply = execute_function(multiply, 5, 3)

    print(f"Addition Result: {result_add}")          # Output: Addition Result: 8
    print(f"Multiplication Result: {result_multiply}")  # Output: Multiplication Result: 15