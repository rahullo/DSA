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
    

list = Linked_List()


arr1 = [4,2,1,3]
for item in arr1:
    list.append(item)



class Solution:
    def insertionSortListMy(self, head):
        arr = []
        curr_node = head

        while curr_node != None:
            arr.append(curr_node.val)
            curr_node = curr_node.next
        
        print(arr)

        l = len(arr)
        new_head = Node()
        curr = new_head
        arr.sort()

        for item in arr:
            curr.next = Node(item)
            curr = curr.next
        
        return new_head.next
    
    def insertionSortList(self, head):
        dummy = Node(0)
        curr = head

        while curr:
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = next

        return dummy.next
        



sol = Solution()
newhead = sol.insertionSortList(list.head)