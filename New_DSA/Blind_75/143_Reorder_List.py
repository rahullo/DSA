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


def printList(head):
    if head == None:
        return 
    
    print(head.val, end='->')
    printList(head.next)


def reorderList(head) -> None:
    arr = []
    curr = head
    while curr:
        arr.append(curr)
        curr = curr.next 
        
    dummy = ListNode()
    curr = dummy
    l = 0
    r = len(arr) - 1
    while l < r:   #[1, 2, 3, 4, 5, 6]
        # print('l', l, ', r', r)

        curr.next = arr[l]
        curr.next.next  = arr[r]
        curr = curr.next.next
        l+=1
        r-=1
    curr.next = None
    return dummy.next

printList(list1)
print('\n')

reorderList(list1)