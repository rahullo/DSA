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
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        
        # Dummy node to handle head changes
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # 1. Check if there are k nodes left to reverse
            kth = self.get_kth(group_prev, k)
            if not kth:
                break
            
            # 2. Setup pointers for the current group reversal
            group_next = kth.next
            prev, curr = kth.next, group_prev.next
            
            # 3. Standard reversal of k nodes
            # Instead of the 'insertion' method, we can use a classic flip here
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 4. Connect the previous group to the new head of this group
            tmp = group_prev.next # The old head (now the tail)
            group_prev.next = kth # The new head
            group_prev = tmp      # Move group_prev to the tail for the next iteration
            
        return dummy.next

    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    

cls = Solution()
reversed = cls.reverseKGroup(head, 2)

while reversed:
    print(reversed.val, "-> ", end='')
    reversed = reversed.next