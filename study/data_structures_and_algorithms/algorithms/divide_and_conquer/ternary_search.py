from typing import List, Optional
import unittest

def ternary_search(arr: List[int], target: int) -> Optional[int]:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if arr[mid1] > target:
            right = mid1 - 1
        elif arr[mid2] < target:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return None

def ternary_search_max(func, left, right, precision=1e-9):
    while right - left > precision:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3

        if func(mid1) < func(mid2):
            left = mid1
        else:
            right = mid2
    return (left + right) / 2

def ternary_search_min(func, left, right, precision=1e-9):
    while right - left > precision:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3

        if func(mid1) > func(mid2):
            left = mid1
        else:
            right = mid2
    return (left + right) / 2

class TestTernarySearchValue(unittest.TestCase):
    def test_ternary_search(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(ternary_search(arr, 5), 4)
        self.assertEqual(ternary_search(arr, 1), 0)
        self.assertEqual(ternary_search(arr, 9), 8)
        self.assertEqual(ternary_search(arr, 10), None)

class TestTernarySearchFuncMax(unittest.TestCase):
    def test_ternary_search_max(self):
        func = lambda x: -(x - 2) ** 2 + 4
        self.assertAlmostEqual(ternary_search_max(func, 0, 4), 2, places=6)

class TestTernarySearchFuncMin(unittest.TestCase):
    def test_ternary_search_min(self):
        func = lambda x: (x - 2) ** 2 + 1
        self.assertAlmostEqual(ternary_search_min(func, 0, 4), 2, places=6)

if __name__ == "__main__":
    unittest.main()
