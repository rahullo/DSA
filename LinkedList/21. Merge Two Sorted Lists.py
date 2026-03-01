class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(list1, list2):
        dummy = ListNode()
        tail = dummy
        
        # Core loop: compare and link. 
        # We iterate only as long as both lists have nodes.
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # Optimization: Once one list is exhausted, we don't need to loop anymore.
        # We simply point the tail to the remaining portion of the non-empty list.
        tail.next = list1 or list2
        
        return dummy.next