class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtIndex(self, val, index):
        currNode = self.head
        newNode = Node(val)
        i = 0
        if index == 0:
            self.insertAtBegin(val)
        else:
            while i < index-1:
                currNode = currNode.next
                i+=1
            if newNode != None:
                temp = currNode.next
                currNode.next = newNode
                newNode.next = temp
            else:
                print("Index Not Available")

    def insertAtEnd(self, val):
        if self.head == None:
            self.insertAtBegin(val)
            return
        newNode = Node(val)
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
        if currNode!=None:
            currNode.next = newNode

    def insert(self, val):
        currNode = self.head
        
        while currNode != None and  currNode.value < val:
            currNode = currNode.next
        if currNode != None:
            newNode = Node(val)
            temp = currNode.next
            currNode.next = newNode
            newNode.next = temp
        else:
            self.insertAtEnd(val)

    def deleteAtStart(self):
        if self.head and self.head.next:
            self.head = self.head.next
        elif self.head and not self.head.next:
            self.head = None
        else:
            print("No node found")
            
    def deleteAtEnd(self):
        currNode = self.head
        previousNode = None
        while currNode.next != None:
            previousNode = currNode
            currNode = currNode.next
        previousNode.next = None
    
    def deleteByValue(self, val):
        currNode = self.head
        previousNode = None
        while currNode.value != val:
            previousNode = currNode
            currNode = currNode.next

        if currNode.next != None and previousNode != None:
            previousNode.next = currNode.next
        elif currNode.next == None:
            previousNode.next = None
        elif previousNode == None:
            self.deleteAtStart()
        

    def printLinkedList(self):
        currNode = self.head
        while currNode != None:
            print(currNode.value, "-->", end="")
            currNode = currNode.next
        print('\n')

linkedList = LinkedList()
linkedList.insertAtBegin(55)
linkedList.insertAtBegin(44)
linkedList.insertAtBegin(33)
linkedList.insertAtBegin(22)
linkedList.insertAtBegin(11)
linkedList.insertAtBegin(1)


linkedList.insertAtIndex(25, 3)
linkedList.insertAtIndex(0, 0)
linkedList.insertAtIndex(66, 8)

linkedList.insert(26)
linkedList.insert(77)

linkedList.printLinkedList()

linkedList.deleteAtStart()
linkedList.deleteAtStart()

linkedList.printLinkedList()

linkedList.deleteByValue(11)

linkedList.printLinkedList()
