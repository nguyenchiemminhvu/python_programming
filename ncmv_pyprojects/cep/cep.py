from typing import List
import math

def cep_50(intervals: List[int], ideal_interval: int = 0) -> int:
    """
    Calculate the CEP 50 value from a list of intervals.

    Parameters:
    intervals (List[int]): A list of interval values.
    ideal_interval (int): The ideal interval value.

    Returns:
    int: The CEP 50 value.
    """
    if not intervals:
        raise ValueError("The intervals list cannot be empty.")

    deviations = [abs(interval - ideal_interval) for interval in intervals]
    deviations.sort()
    index_50 = math.ceil(0.5 * len(deviations)) - 1
    return deviations[index_50]

def cep_68(intervals: List[int], ideal_interval: int = 0) -> int:
    """
    Calculate the CEP 68 value from a list of intervals.

    Parameters:
    intervals (List[int]): A list of interval values.
    ideal_interval (int): The ideal interval value.

    Returns:
    int: The CEP 68 value.
    """
    if not intervals:
        raise ValueError("The intervals list cannot be empty.")

    deviations = [abs(interval - ideal_interval) for interval in intervals]
    deviations.sort()
    index_68 = math.ceil(0.68 * len(deviations)) - 1
    return deviations[index_68]

def cep_95(intervals: List[int], ideal_interval: int = 0) -> int:
    """
    Calculate the CEP 95 value from a list of intervals.

    Parameters:
    intervals (List[int]): A list of interval values.
    ideal_interval (int): The ideal interval value.

    Returns:
    int: The CEP 95 value.
    """
    if not intervals:
        raise ValueError("The intervals list cannot be empty.")

    deviations = [abs(interval - ideal_interval) for interval in intervals]
    deviations.sort()
    index_95 = math.ceil(0.95 * len(deviations)) - 1
    return deviations[index_95]

def cep_99(intervals: List[int], ideal_interval: int = 0) -> int:
    """
    Calculate the CEP 99 value from a list of intervals.

    Parameters:
    intervals (List[int]): A list of interval values.
    ideal_interval (int): The ideal interval value.

    Returns:
    int: The CEP 99 value.
    """
    if not intervals:
        raise ValueError("The intervals list cannot be empty.")

    deviations = [abs(interval - ideal_interval) for interval in intervals]
    deviations.sort()
    index_99 = math.ceil(0.99 * len(deviations)) - 1
    return deviations[index_99]

def cep_100(intervals: List[int], ideal_interval: int = 0) -> int:
    """
    Calculate the CEP 100 value from a list of intervals.

    Parameters:
    intervals (List[int]): A list of interval values.
    ideal_interval (int): The ideal interval value.

    Returns:
    int: The CEP 100 value.
    """
    if not intervals:
        raise ValueError("The intervals list cannot be empty.")

    deviations = [abs(interval - ideal_interval) for interval in intervals]
    deviations.sort()
    index_100 = len(deviations) - 1
    return deviations[index_100]
