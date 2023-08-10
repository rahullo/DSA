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
    
    def mergeTwoLists(self, head1, head2):
        if not head1 or not head2:
            return head1 if head1 else head2
        if head1.val > head2.val:
            head1, head2 = head2, head1
            head1.next = self.mergeTwoLists(head1.next, head2)
        return head1

    def reverse(self, head):
        prev = None
        curr = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def remove(self, head, val):
        if head == None:
            return head

        if head.val == val:
            temp = head.next
            self.head = head.next
            return head


        curr = head.next
        prev = head
        while curr != None:
            if curr.val == val:
                prev.next = curr.next

            prev = curr
            curr = curr.next

            

link = Linked_List()
link.append(1)
link.append(4)
link.append(2)
link.append(3)
link.append(5)
link.append(3)
link.printList(link.head)
# link.reverse(link.head)
print('\n')
link.remove(link.head, 3)
print('\n')

link.printList(link.head)

# link2 = Linked_List()
# link2.append(13)
# link2.append(12)
# link2.append(15)
# link2.append(11)
# link2.append(14)
# print('\n')
# link2.printList(link2.head)
# print('\n')
# # print(link.mergeTwoSortedArray(link.head, link2.head))
# link.printList(link.mergeTwoLists(link.head, link2.head))



        
