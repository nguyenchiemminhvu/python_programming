from typing import List, Dict, Tuple, Union, Any, Optional

# List example
def process_numbers(numbers: List[int]) -> int:
    """Returns the sum of a list of integers."""
    return sum(numbers)

print(process_numbers([1, 2, 3, 4, 5]))  # Output: 15

# Dict example
def get_student_grades(grades: Dict[str, float]) -> float:
    """Returns the average grade from a dictionary of student grades."""
    return sum(grades.values()) / len(grades) if grades else 0.0

print(get_student_grades({'Alice': 85.5, 'Bob': 90.0, 'Charlie': 78.0}))  # Output: 84.5

# Tuple example
def get_coordinates() -> Tuple[float, float]:
    """Returns a tuple representing coordinates (latitude, longitude)."""
    return (37.7749, -122.4194)  # Example coordinates for San Francisco

print(get_coordinates())  # Output: (37.7749, -122.4194)

# Union example
def process_value(value: Union[int, float]) -> str:
    """Returns a string representation of the value."""
    return f"The value is: {value}"

print(process_value(42))          # Output: The value is: 42

# Any example
def handle_any(value: Any) -> str:
    """Returns a string representation of any value."""
    return f"Received value: {value}"

print(handle_any("Hello, World!"))  # Output: Received value: Hello, World!

# Optional example
def find_item(items: List[str], item: str) -> Optional[int]:
    """Returns the index of the item if found, otherwise None."""
    try:
        return items.index(item)
    except ValueError:
        return None

print(find_item(['apple', 'banana', 'cherry'], 'banana'))  # Output: 1
print(find_item(['apple', 'banana', 'cherry'], 'orange'))  # Output: None