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
            new_node.next = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
            self.length +=1


    def printList(self):
        curr = self.head
        while (True):
            print(curr.val, end=' ')
            curr = curr.next
            if curr == self.head:
                break

    def insert_in_biggining(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head  = new_node
        self.tail.next = new_node
        self.length+=1

    def partition(self, start, end):
        if(start == end or start == None or end == None):
            return start
        curr = start
        prev = start
        pivot = end.val

        while start != end:
            if start.val < pivot:
                prev = curr
                curr.val, start.val = start.val, curr.val
                curr = curr.next
            start = start.next
            # if(curr == self.head):
            #     break
        temp = curr.val
        curr.val = end.val
        end.val = temp
        return prev

    def sort(self, start, end):
        if start == None or start == end or start == end.next:
            return
        
        prev_node = self.partition(start, end)
        self.sort(start, prev_node)

        if(prev_node != None and start == prev_node):
            self.sort(prev_node.next, end)
        elif(prev_node != None and prev_node.next == None):
            self.sort(prev_node.next.next, end)

    def insertBetweenNodes(self, value, val):
        new_node = Node(value)
        curr = self.head
        while(curr.val != val):
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

    def delete(self, val):
        curr = self.head
        if self.head == None:
            return 

        if curr.val == val and self.head.next == curr:
            self.head = None

        last = self.head
        d = None   


        if (curr.val == val):
            while last.next != self.head:
                last = last.next

            last.next = self.head.next
            self.head = last.next
            

        while last.next != self.head and last.next.val != val:
            last = last.next

        if(last.next.val == val):
            d = last.next
            last.next = d.next

        return self.head

    def countNodes(self):
        curr = self.head.next
        count = 1
        while curr != self.head:
            count += 1
            curr = curr.next
        return count


    

link = Linked_List()
link.append(2)
# link.delete(2)
link.append(8)
link.append(9)
link.append(1)
link.append(4)
link.printList()
print('\n')
# link.sort(link.head, link.tail)
link.insertBetweenNodes(11, 9)
link.delete(2)
link.printList()
print('\n')
print(link.countNodes())
print('\n')
link.delete(11)
link.printList()
print('\n')
print(link.countNodes())


