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
        curr = self.head
        while curr != None:
            print(curr.val, end=' ')
            curr = curr.next
    

    def reverseList(self):
        curr = self.head
        prev = None
        while(curr != None):
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        self.head = prev

    def removeLoop(self, head):
        curr = head.next
        while curr.next != head:
            curr = curr.next

        curr
        

link = Linked_List()
link.append(2)
link.append(8)
link.append(4)
link.append(1)
link.append(0)
link.printList()
link.reverseList()
print('\n')
link.printList()

