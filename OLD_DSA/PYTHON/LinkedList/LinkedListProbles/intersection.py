from numpy import append


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length +=1
    
    def printList(self):
        head = self.head
        while head != None:
            print(head.val, end=" ")
            head = head.next
        print('\n')


def intersection(link1, link2):
    dummy = Node((link1.val if link2.val > link1.val else link2.val))
    tail = dummy
    dummy.next = None

    while(link1 != None or link2 != None):
        if(link1.next.val == link2.next.val):
            tail.next = append((tail.next), link1.val)
            tail = tail.next
            link1 = link1.next
            link2 = link2.next

        elif(link1.val < link2.val):
            link1 = link1.next

        else:
            link2 = link2.next

    return dummy.next


link = Linked_List()
link.append(1)
link.append(2)
link.append(3)
link.append(4)
link.append(5)
link.append(6)
link.printList()

link2 = Linked_List()
link2.append(1)
link2.append(12)
link2.append(3)
link2.append(14)
link2.append(5)
link2.append(16)
link2.printList()

head = intersection(link, link2)
link.printList(head)

