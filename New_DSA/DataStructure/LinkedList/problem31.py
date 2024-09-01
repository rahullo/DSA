#If the head of a linked list is pointing to kth element, then how will you get the elements before kth element?


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, node, data):
        if node is None:
            return
        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next
        if node.next:
            node.next.prev = new_node
        node.next = new_node

    def delete(self, node):
        if node is None or (node is not self.head and node is not self.tail):
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.insert_after(dll.head.next, 4)
dll.print_list()  # Output: 0 1 4 2 3
dll.delete(dll.head.next)
dll.print_list()  # Output: 0 4 2 3

def display(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print(None, '\n')

