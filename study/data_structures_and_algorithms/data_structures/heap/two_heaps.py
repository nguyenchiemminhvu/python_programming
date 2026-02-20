import heapq

class TwoHeaps:
    def __init__(self):
        self.min_heap = [] # store the larger half of the numbers
        self.max_heap = [] # store the smaller half of the numbers

    def insert(self, value):
        if not self.min_heap or value >= self.min_heap[0]:
            heapq.heappush(self.min_heap, value)
        else:
            heapq.heappush(self.max_heap, -value)

        # balance the heaps
        if len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
    
    def get_median(self):
        if not self.min_heap and not self.max_heap:
            raise ValueError("No numbers are available")

        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2

        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        return -self.max_heap[0]

# testing

import unittest

class TestTwoHeaps(unittest.TestCase):
    def test_median(self):
        th = TwoHeaps()
        th.insert(1)
        self.assertEqual(th.get_median(), 1)
        th.insert(2)
        self.assertEqual(th.get_median(), 1.5)
        th.insert(3)
        self.assertEqual(th.get_median(), 2)
        th.insert(4)
        self.assertEqual(th.get_median(), 2.5)
        th.insert(5)
        self.assertEqual(th.get_median(), 3)
        th.insert(6)
        self.assertEqual(th.get_median(), 3.5)
        th.insert(7)
        self.assertEqual(th.get_median(), 4)
        th.insert(8)
        self.assertEqual(th.get_median(), 4.5)

if __name__ == "__main__":
    unittest.main()