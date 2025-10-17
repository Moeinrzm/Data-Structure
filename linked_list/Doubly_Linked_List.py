class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
         new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def insert_at_beginning(self, data):
         new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete_node(self, key):
         current = self.head
        if not current:
            print("List is empty.")
            return
        while current and current.data != key:
            current = current.next
        if not current:
            print(f"Node with data {key} not found.")
            return
        if current.prev:
            current.prev.next = current.next
        else:  
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        current = None
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):    
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
