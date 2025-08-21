from abc import ABC, abstractmethod

class iterator(ABC):
    @abstractmethod
    def get_iterator(self):
        """Return an iterator object."""
        pass
    
    @abstractmethod
    def reset_iterator(self):
        """Reset the iterator to the beginning."""
        pass
    
    def get_next(self):
        """Return the next item in the iteration."""
        pass
    
    def has_next(self):
        """Return True if there are more items to iterate over, False otherwise."""
        pass

class iterable(ABC):
    @abstractmethod
    def get_iterator(self):
        """Return an iterator object."""
        pass
    
class concrete_iterator(iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def get_iterator(self):
        return self
    
    def reset_iterator(self):
        self._index = 0

    def get_next(self):
        if self.has_next():
            item = self._collection[self._index]
            self._index += 1
            return item
        raise StopIteration("No more items to iterate over.")

    def has_next(self):
        return self._index < len(self._collection)

class concrete_iterable(iterable):
    def __init__(self, collection):
        self._collection = collection

    def get_iterator(self):
        return concrete_iterator(self._collection)

if __name__ == "__main__":
    # Example usage
    collection = [1, 2, 3, 4, 5]
    iterable_obj = concrete_iterable(collection)
    iterator_obj = iterable_obj.get_iterator()

    while iterator_obj.has_next():
        print(iterator_obj.get_next())

    iterator_obj.reset_iterator()
    while iterator_obj.has_next():
        print(iterator_obj.get_next())