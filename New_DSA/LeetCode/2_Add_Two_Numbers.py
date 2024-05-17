import sys
import os

# Add folder_a to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DataStructure')))

# Now you can import MyClass from module_a
from linkedList import LinkedList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = LinkedList()
l1.insertAtEnd(2)
l1.insertAtEnd(4)
l1.insertAtEnd(3)

l2 = LinkedList()
l2.insertAtEnd(5)
l2.insertAtEnd(6)
l2.insertAtEnd(4)

l1.printLinkedList()
l2.printLinkedList()


def addTwoNumbers(l1, l2):
    # Initialize a dummy node and a current node pointing to it
    dummy = ListNode()
    current = dummy
    carry = 0

    # Traverse both lists
    while l1 or l2 or carry:
        # Get the values from the current nodes (if present)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Compute the new sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        new_val = total % 10

        # Create a new node with the computed value
        current.next = ListNode(new_val)
        current = current.next

        # Move to the next nodes (if present)
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # The result is in the dummy.next
    return dummy.next

# Helper function to create a linked list from a list of values
def createLinkedList(vals):
    dummy = ListNode()
    current = dummy
    for val in vals:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list of values
def linkedListToList(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage:
l1 = createLinkedList([2, 4, 3])
l2 = createLinkedList([5, 6, 4])
result = addTwoNumbers(l1, l2)
print(linkedListToList(result))  # Output: [7, 0, 8]

l1 = createLinkedList([0])
l2 = createLinkedList([0])
result = addTwoNumbers(l1, l2)
print(linkedListToList(result))  # Output: [0]

l1 = createLinkedList([9, 9, 9, 9, 9, 9, 9])
l2 = createLinkedList([9, 9, 9, 9])
result = addTwoNumbers(l1, l2)
print(linkedListToList(result))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]
