from typing import List
import heapq
import math

def cep_50(values: List[int], ideal_value: int = 0) -> int:
    """
    Calculate the CEP 50 value from a list of values.

    Parameters:
    values (List[int]): A list of interval values.
    ideal_value (int): The ideal interval value.

    Returns:
    int: The CEP 50 value.
    """
    if not values:
        raise ValueError("The values list cannot be empty.")

    deviations = [abs(interval - ideal_value) for interval in values]
    deviations.sort()
    index_50 = math.ceil(0.5 * len(deviations)) - 1
    return deviations[index_50]

def cep_68(values: List[int], ideal_value: int = 0) -> int:
    """
    Calculate the CEP 68 value from a list of values.

    Parameters:
    values (List[int]): A list of interval values.
    ideal_value (int): The ideal interval value.

    Returns:
    int: The CEP 68 value.
    """
    if not values:
        raise ValueError("The values list cannot be empty.")

    deviations = [abs(interval - ideal_value) for interval in values]
    deviations.sort()
    index_68 = math.ceil(0.68 * len(deviations)) - 1
    return deviations[index_68]

def cep_95(values: List[int], ideal_value: int = 0) -> int:
    """
    Calculate the CEP 95 value from a list of values.

    Parameters:
    values (List[int]): A list of interval values.
    ideal_value (int): The ideal interval value.

    Returns:
    int: The CEP 95 value.
    """
    if not values:
        raise ValueError("The values list cannot be empty.")

    deviations = [abs(interval - ideal_value) for interval in values]
    deviations.sort()
    index_95 = math.ceil(0.95 * len(deviations)) - 1
    return deviations[index_95]

def cep_99(values: List[int], ideal_value: int = 0) -> int:
    """
    Calculate the CEP 99 value from a list of values.

    Parameters:
    values (List[int]): A list of interval values.
    ideal_value (int): The ideal interval value.

    Returns:
    int: The CEP 99 value.
    """
    if not values:
        raise ValueError("The values list cannot be empty.")

    deviations = [abs(interval - ideal_value) for interval in values]
    deviations.sort()
    index_99 = math.ceil(0.99 * len(deviations)) - 1
    return deviations[index_99]

def cep_100(values: List[int], ideal_value: int = 0) -> int:
    """
    Calculate the CEP 100 value from a list of values.

    Parameters:
    values (List[int]): A list of interval values.
    ideal_value (int): The ideal interval value.

    Returns:
    int: The CEP 100 value.
    """
    if not values:
        raise ValueError("The values list cannot be empty.")

    deviations = [abs(interval - ideal_value) for interval in values]
    deviations.sort()
    index_100 = len(deviations) - 1
    return deviations[index_100]

class cep_analyzer:
    def __init__(self, percent, ideal_value: int = 0):
        self.min_heap = []
        self.max_heap = []
        self.percent = percent
        self.ideal_value = ideal_value
    
    def add_sample(self, sample):
        deviation = abs(sample - self.ideal_value)
        if not self.max_heap or deviation <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -deviation)
        else:
            heapq.heappush(self.min_heap, deviation)
        
        total_samples = len(self.max_heap) + len(self.min_heap)
        desired_max_heap_size = int(total_samples * self.percent)
        while len(self.max_heap) > desired_max_heap_size:
            moved_sample = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, moved_sample)
        while len(self.max_heap) < desired_max_heap_size:
            moved_sample = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -moved_sample)
    
    def get_cep(self):
        if not self.min_heap:
            return None
        return self.min_heap[0]
