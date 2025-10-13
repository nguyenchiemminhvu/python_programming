from typing import List

def heapify(arr:List[int], n:int, i:int, reverse:bool=False) -> None:
    pivot = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and ((arr[left] > arr[pivot]) != reverse):
        pivot = left
    if right < n and ((arr[right] > arr[pivot]) != reverse):
        pivot = right
    if pivot != i:
        arr[i], arr[pivot] = arr[pivot], arr[i]
        heapify(arr, n, pivot, reverse)

def build_heap(arr:List[int], reverse:bool=False) -> None:
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, reverse)

def add_to_heap(arr:List[int], key:int, reverse:bool=False) -> None:
    arr.append(key)
    index = len(arr) - 1
    parent = (index - 1) // 2
    while index > 0 and ((arr[index] > arr[parent]) != reverse):
        arr[index], arr[parent] = arr[parent], arr[index]
        index = parent
        parent = (index - 1) // 2

def remove_from_head(arr:List[int], reverse:bool=False) -> int:
    if len(arr) == 0:
        raise IndexError("remove_from_head(): empty heap")
    root = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    heapify(arr, len(arr), 0, reverse)
    return root

def heap_sort(arr:List[int], reverse:bool=False) -> List[int]:
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, reverse)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, reverse)
    return arr