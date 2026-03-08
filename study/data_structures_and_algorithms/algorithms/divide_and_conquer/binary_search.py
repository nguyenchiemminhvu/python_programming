from typing import List, Optional
import unittest

def binary_search(arr: List[int], target: int) -> Optional[int]:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(binary_search(arr, 5), 4)
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 9), 8)
        self.assertEqual(binary_search(arr, 10), None)

if __name__ == "__main__":
    unittest.main()
