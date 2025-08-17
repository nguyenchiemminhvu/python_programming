from abc import ABC, abstractmethod
import time

class sorter:
    def __init__(self):
        pass

    def sort(self, data):
        return sorted(data)

class upgraded_sorter():
    def __init__(self):
        self.old_sorter = sorter()

    def sort_and_prefix_sum(self, data):
        sorted_data = self.old_sorter.sort(data)
        prefix_sum = [sum(sorted_data[:i+1]) for i in range(len(sorted_data))]
        return sorted_data, prefix_sum

class simple_algo_system:
    def __init__(self):
        self.sorter = upgraded_sorter()

    def sort_and_prefix_sum(self, data):
        return self.sorter.sort_and_prefix_sum(data)

if __name__ == "__main__":
    algo = simple_algo_system()
    data = [5, 3, 8, 6, 2]
    sorted_data, prefix_sum = algo.sort_and_prefix_sum(data)
    print("Sorted Data:", sorted_data)
    print("Prefix Sum:", prefix_sum)