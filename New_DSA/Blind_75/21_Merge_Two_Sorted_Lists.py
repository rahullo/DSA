class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(6)
list1.next.next.next = ListNode(8)
list1.next.next.next.next = ListNode(10)
list1.next.next.next.next.next = ListNode(16)

list2 = ListNode(2)
list2.next = ListNode(5)
list2.next.next = ListNode(7)
list2.next.next.next = ListNode(9)
# list1.next.next.next.next = ListNode(5)
# list1.next.next.next.next.next = ListNode(6)

def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print('\n')


def mergeTwoLists(list1, list2):
    dummy = node = ListNode()

    while list1 and list2:
        if list1.val <= list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next 
        node = node.next
    
    node.next = list1 or list2

    return dummy.next

def mergeTwoListsRecusion(list1, list2):


l = mergeTwoListsRecusion(list1, list2)
printList(l)