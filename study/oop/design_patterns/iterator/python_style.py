class collection:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx < len(self.items):
            val = self.items[self.idx]
            self.idx += 1
            return val
        raise StopIteration

if __name__ == "__main__":
    coll = collection()
    coll.add(1)
    coll.add(2)
    coll.add(3)

    for item in coll:
        print(item)