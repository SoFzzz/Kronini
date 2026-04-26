class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            self.current = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def forward(self):
        if self.current:
            self.current = self.current.next
        return self.get_current()

    def backward(self):
        if self.current:
            self.current = self.current.prev
        return self.get_current()

    def get_current(self):
        return self.current.data if self.current else None
