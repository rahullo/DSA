class XORLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.npx = 10

class XORLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        print("Entered")
        new_node = XORLinkedListNode(data)
        new_node.npx = self.head
        if self.head:
            print(self.head.npx, new_node.npx)
            self.head.npx = new_node ^ self.head.npx
        self.head = new_node

    def get_elements_before_kth(self, k):
        if k <= 0:
            return []
        current = self.head
        prev = None
        for _ in range(k - 1):
            prev = current
            current = current.npx ^ prev
        return self.get_elements_before(prev)

    def get_elements_before(self, node):
        elements = []
        while node:
            elements.append(node.data)
            next_node = node.npx ^ elements[-1]
            node = next_node
        return elements[::-1]  # Reverse the list to get the correct order

# Example usage
xor_list = XORLinkedList()
xor_list.insert_at_beginning(5)
xor_list.insert_at_beginning(4)
xor_list.insert_at_beginning(3)
xor_list.insert_at_beginning(2)
xor_list.insert_at_beginning(1)

k = 3
elements_before_kth = xor_list.get_elements_before_kth(k)
print("Elements before the kth element:", elements_before_kth)