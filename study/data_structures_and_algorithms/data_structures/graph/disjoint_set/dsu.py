from typing import List, Dict

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = n
    
    def unite(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_y] += 1
    
    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def groups(self) -> Dict[int, List[int]]:
        g : Dict[int, List[int]] = {}
        for i in range(self.size):
            root = self.find(i)
            if root not in g:
                g[root] = []
            g[root].append(i)
        return g