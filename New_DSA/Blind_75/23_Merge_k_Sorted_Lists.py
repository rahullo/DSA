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


def printList(head):
    if head == None:
        return
    
    print(head.val, end='->')
    printList(head.next)

def mergeKList(lists):
    node = dummy = ListNode()

    list1 = lists[0]
    list2 = lists[1]
    list3 = lists[2]
    
    while list1 and list2 and list3:
        if list1.val < list2.val and list1.val < list3.val:
            node.next = list1
            list1 = list1.next
        elif list2.val < list1.val and list2.val < list3.val:
            node.next = list2
            list2 = list2.next
        else:
            node.next = list3
            list3 = list3.next 
    return dummy.next


printList(list1)
print('\n')
printList(list2)
print('\n')
printList(list3)
print('\n')

printList(mergeKList([list1, list2, list3]))
