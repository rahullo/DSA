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
            self.tail = self.head
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
    

list1 = Linked_List()
list1.append(5)
list1.append(8)
list1.append(1)
list1.append(9)
list1.append(2)
list1.append(0)

def nextLargerNodes(head):
    arr = []
    curr = head
    while curr != None:
        maxi = curr.val
        mcurr = curr.next
        while mcurr != None:
            if maxi < mcurr.val:
                maxi = mcurr.val
        
