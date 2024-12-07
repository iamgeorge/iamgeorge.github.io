class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next

    def next(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current.next
            current = current.next
        return None

    def previous(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current.prev
            current = current.next
        return None

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")


# Example usage:


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)

print("Initial linked list:")
ll.traverse()

ll.delete(2)

print("Linked list after deleting 2:")
ll.traverse()

next_node = ll.next(1)
print("Next node after 1:", next_node.data if next_node else None)

prev_node = ll.previous(3)
print("Previous node before 3:", prev_node.data if prev_node else None)
