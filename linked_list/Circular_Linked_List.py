class Node:
   def __init__(self, data):
       self.data = data
       self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head 
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        current = self.head
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        prev = None      
        if current.data == key:
            if current.next == self.head:
                self.head = None
                return
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = current.next
            self.head = current.next
            return
        prev = current
        current = current.next
        while current != self.head:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print(f"node with value {key} not found.")

    def display(self):
        nodes = []
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while True:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        print(" -> ".join(nodes) + " -> (back to head)")
