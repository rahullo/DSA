#Given two sorted Linked Lists, we need to merge them into the third list in sorted order.

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(9)
head.next.next.next.next = Node(11)
head.next.next.next.next.next = Node(16)

link = Node(2)
link.next = Node(3)
link.next.next = Node(7)
link.next.next.next = Node(14)
link.next.next.next.next = Node(15)
link.next.next.next.next.next = Node(19)

def display(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print(None, '\n')



def mergeTwoSortedLinkedListRecursively(list1, list2):
    if not list1:
        return list2
    elif not list2:
        return list1
    
    head = Node(0)
    if(list1.data <= list2.data):
        head = list1
        head.next = mergeTwoSortedLinkedListRecursively(list1.next, list2)
    else:
        head = list2
        head.next = mergeTwoSortedLinkedListRecursively(list1, list2.next)

    return head



def mergeTwoSortedLinkedListRecursively_2(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    
    lil, big = (list1, list2) if list1.data <= list2.data else (list2, list1)
    lil.next = mergeTwoSortedLinkedListRecursively_2(lil.next, big)
    return lil

def mergeTwoList(list1, list2):
    node = dummy = Node(0)
    while list1 and list2:
        if list1.data <= list2.data:
            node.next = list1
            list1 = list1.next 
        else:
            node.next = list2 
            list2 = list2.next 
        node = node.next 
    node.next = list1 or list2

    return dummy.next

display(head)
# print('\n')
display(link)
# print('\n')
display(mergeTwoList(head, link))