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


    def printList(self, head):
        curr = head
        while curr != None:
            print(curr.val, end=' ')
            curr = curr.next
    
    def count(self, head):
        curr = head
        count = 0
        while curr != None:
            count +=1
            curr = curr.next

        return count

    def middleNode(self, head):
        curr = head
        length = self.count(head)
        mid = length // 2
        for i in range(mid):
            curr = curr.next
        return curr
            

link = Linked_List()
link.append(1)
link.append(2)
link.append(3)
link.append(4)
link.append(5)
# link.append(6)

link.printList(link.head)
print('\ncount ')
print(link.count(link.head))
mid = link.middleNode(link.head)
link.printList(mid)



