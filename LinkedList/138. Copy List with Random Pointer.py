class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head: return None
        
        # 1. Create copy nodes and weave them into the original list
        # A -> B becomes A -> A' -> B -> B'
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
        
        # 2. Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # 3. Separate the two lists
        old_head = head
        new_head = head.next
        curr = new_head
        
        while old_head:
            old_head.next = old_head.next.next
            curr.next = curr.next.next if curr.next else None
            old_head = old_head.next
            curr = curr.next
            
        return new_head