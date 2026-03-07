# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        # Step 1: Set up dummy to handle head changes
        dummy = ListNode(0, head)
        prev = dummy
        
        # Step 2: Move prev to the node just before the sub-list
        for _ in range(left - 1):
            prev = prev.next
        
        # curr is the first node of the sub-list to be reversed
        curr = prev.next
        
        # Step 3: Reverse the nodes by shifting them one by one
        # We do this (right - left) times
        for _ in range(right - left):
            # nxt is the node we are moving to the front of the sub-list
            nxt = curr.next
            
            # 1. curr points to the node after nxt
            curr.next = nxt.next
            
            # 2. nxt points to the current head of the reversed part
            nxt.next = prev.next
            
            # 3. prev points to nxt (nxt becomes the new head of sub-list)
            prev.next = nxt
            
        return dummy.next

cls = Solution()
reversed = cls.reverseBetween(head, 2, 4)

while reversed:
    print(reversed.val, "-> ", end='')
    reversed = reversed.next