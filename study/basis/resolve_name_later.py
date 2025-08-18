from dataclasses import dataclass, field

@dataclass
class list_node:
    data : int
    next : "list_node" = field(default=None, repr=False) # list_node type is resolved later

class linked_list:
    def __init__(self):
        self.head : list_node = None
        self.tail : list_node = None

if __name__ == "__main__":
    ll = linked_list()
    ll.head = list_node(1)
    ll.tail = ll.head