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
    

    def convertToCircular(self):
        curr = self.head
        while(curr.next !=None):
            curr = curr.next
        curr.next = self.head

    def printCircularList(self):
        curr = self.head
        while True:
            print(curr.val, end=" ")
            curr = curr.next
            if curr == self.head:
                break


link = Linked_List()
link.append(1)
link.append(2)
link.append(3)
link.append(4)
link.append(5)
link.append(6)
link.printList()
link.convertToCircular()
print('\n')
link.printCircularList()

