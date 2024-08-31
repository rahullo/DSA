class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)
list1.next.next.next.next.next = ListNode(6)
list1.next.next.next.next.next.next = ListNode(7)
list1.next.next.next.next.next.next.next = ListNode(8)
list1.next.next.next.next.next.next.next.next = list1.next.next.next


def printList(head):
    if head == None:
        return
    
    printList(head.next)
    print(head.val, end='->')

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return True
    return False

print(hasCycle(list1))