class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(6)
list1.next.next.next = ListNode(9)
list1.next.next.next.next = ListNode(15)

list2 = ListNode(2)
list2.next = ListNode(5)
list2.next.next = ListNode(7)
list2.next.next.next = ListNode(11)


list3 = ListNode(1)
list3.next = ListNode(3)
list3.next.next = ListNode(8)
list3.next.next.next = ListNode(12)
list3.next.next.next.next = ListNode(13)
list3.next.next.next.next.next = ListNode(14)

class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        
        return dummy.next

def printList(head):
    if head == None:
        return
    
    print(head.val, end='->')
    printList(head.next)

printList(list1)
print('\n')
printList(list2)
print('\n')
printList(list3)
print('\n')

s = Solution()

printList(s.mergeKLists([list1, list2, list3]))
