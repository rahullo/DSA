from tracemalloc import start


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
        while(curr != None):
            print(curr.val, end=" ")
            curr= curr.next


    def partition(self, start, end):
        if (start == end or start == None or start == None):
            return start

        prev_node = start
        curr = start
        pivot = end.val

        while (start != end):
            if start.val < pivot:
                prev_node = curr
                temp = curr.val
                curr.val = start.val
                start.val = temp
                curr = curr.next
            start = start.next

        temp = curr.val
        curr.val = end.val
        end.val = temp
        return prev_node

    def sort(self, start, end):
        if start == None or start == end or start == end.next:
            return
        
        prev_node = self.partition(start, end)
        self.sort(start, prev_node)

        if(prev_node != None and start == prev_node):
            self.sort(prev_node.next, end)
        elif(prev_node != None and prev_node.next == None):
            self.sort(prev_node.next.next, end)


    


link = Linked_List()   
link.append(2)
link.append(6)
link.append(9)
link.append(1)
link.append(3)
link.append(0)

link.printList()
link.sort(link.head, link.tail)
print('\n')
link.printList()


