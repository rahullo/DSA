from unicodedata import decimal


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

    def binary2int(self, binary): 
        int_val, i, n = 0, 0, 0
        while(binary != 0): 
            a = binary % 10
            int_val = int_val + a * pow(2, i) 
            binary = binary//10
            i += 1
        return int_val
    
    def getDecimalValue(self, head):
        curr = head
        sum = 0
        while curr != None:
            sum = sum * 10 + curr.val
            curr = curr.next

        num = self.binary2int(sum)

        return num



link = Linked_List()
link.append(1)
link.append(0)
link.append(1)

link.printList()
print(link.getDecimalValue(link.head))
