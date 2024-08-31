# find the merger point of two linked list whose length of both is unknown and head known

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


list2 = Node(11)
list2.next = Node(22)
list2.next.next = Node(33)
list2.next.next.next = Node(44)
list2.next.next.next.next = Node(55)
list2.next.next.next.next.next = Node(66)
list2.next.next.next.next.next.next = Node(77)
list2.next.next.next.next.next.next.next  = Node(88)

list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = list2.next.next.next.next


def display(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print(None, '\n')


display(list2)
display(list1)

def mergerPoint(list1, list2):
    hashMap = {}
    curr1 = list1
    while curr1:
        hashMap[curr1] = True
        curr1 = curr1.next 
    
    curr2 = list2
    while curr2:
        if curr2 in hashMap:
            return curr2
        curr2 = curr2.next 

    return 'No Junction'

print(mergerPoint(list1, list2).data)
