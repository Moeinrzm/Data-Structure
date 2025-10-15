class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        current = self.head
        if current is None:
            print("List is empty.")
            return
        if current.data == key:
            self.head = current.next
            current = None
            return
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next

        if current is None:
            print(f"node with data {key} not found.")
            return

        previous.next = current.next
        current = None

    def search(self, key):
        current = self.head
        pos = 0
        while current:
            if current.data == key:
                return pos
            position += 1
            current = current.next
        return -1 

    def display(self):
        current = self.head
        if not current:
            print("Linked list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
