class custom_list_node:
    def __init__(self, value=0, next:'custom_list_node'=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        s = ""
        current = self
        while current:
            s += f"{current.value} -> "
            current = current.next
        s += "None"
        return s

def test_custom_linked_list():
    node1 = custom_list_node(1)
    node2 = custom_list_node(2)
    node3 = custom_list_node(3)
    print(node1)

    node1.next = node2
    node2.next = node3

    assert node1.value == 1
    assert node1.next.value == 2
    assert node1.next.next.value == 3
    assert node1.next.next.next is None

def test_custom_linked_list_adding_nodes():
    head = custom_list_node(1)
    current = head
    for i in range(2, 6):
        current.next = custom_list_node(i)
        current = current.next

    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next

    assert values == [1, 2, 3, 4, 5]
    print(head)

def test_custom_linked_list_removing_nodes():
    head = custom_list_node(1)
    current = head
    for i in range(2, 6):
        current.next = custom_list_node(i)
        current = current.next

    # Remove node with value 3
    current = head
    if current.value == 3:
        head = current.next 
    else:
        while current and current.next:
            if current.next.value == 3:
                current.next = current.next.next
                break
            current = current.next

    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next

    assert values == [1, 2, 4, 5]
    print(head)

if __name__ == "__main__":
    test_custom_linked_list()
    test_custom_linked_list_adding_nodes()
    test_custom_linked_list_removing_nodes()