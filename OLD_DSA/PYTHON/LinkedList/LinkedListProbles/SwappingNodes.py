
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Linked_List:
#     def __init__(self):
#         self.head = None
#         self.tail = self.head
#         self.length = 0

#     def append(self, value):
#         new_node = Node(value)
#         if self.head == None:
#             self.head = new_node
#             self.tail = new_node
#             self.length = 1
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#             self.length +=1

#     def printList(self, head):
#         current_node = head
#         while current_node != None:
#             print(current_node.val, end=" ")
#             current_node = current_node.next
#         print("\n")


    ###Removing duplicate of sorted List
    # def sorting(self, head):
    #     current_node = head
    #     while current_node.next != None:
    #         if(current_node.val == current_node.next.val):
    #             current_node.next = current_node.next.next
    #         else:
    #             current_node = current_node.next

    # def sorting(self, head):
    #     current_node = head
    #     next_node = None
        
    #     while(current_node.next != None):
    #         next_node= current_node
    #         while(next_node != None):
    #             if current_node.val == next_node.val:
    #                 current_node.next = current_node.next.next
    #             next_node = next_node.next

    #         current_node = current_node.next

    # def sorting(self, head):
    #     if head.val > head.next.val:
        #     temp = head
        #     head = head.next
        #     head.next = temp
            
        # previous_node = head
        # current = head
        # next_node = None
        
        # while current != None:
        #     next_node = current
        #     print('1 loop')
        #     while next_node != None:
        #         print('\t2 loop')
        #         if next_node.val > next_node.next.val:
        #             print("\t\t" ,'if',current.val, next_node.val)
        #             temp = current
        #             current = next_node
        #             next_node = temp
        #             next_node = next_node.next
        #         else:
        #             print("\t\t",'else')
        #             next_node = next_node.next
        #     current = current.next
        # return head
    # def Swapping(self, x, y):
    #     if x == y:
    #         return

    #     prevX = None
    #     currX = self.head
    #     while currX != None and currX.val != x:
    #         prevX = currX
    #         currX = currX.next

    #     prevY = None
    #     currY = self.head
    #     while currY != None and currY.val != y:
    #         prevY = currY
    #         currY = currY.next

    #     if currX ==None or currY == None:
    #         return
        
    #     if prevX != None:
    #         prevX.next = currY
    #     else:
    #         self.head = currY

    #     if prevY != None:
    #         prevY.next = currX
    #     else:
    #         self.head = currX

    #     temp = currX.next
    #     currX.next = currY.next
    #     currY.next = temp   

            
    # def findinglength(self):
    #     head = self.head
    #     length = 1
    #     while head.next != None:
    #         head = head.next
    #         length +=1

    #     return length

    # def pairWiseSwap(self):
    #     temp = self.head

    #     if temp is None:
    #         return

    #     while (temp and temp.next):
    #         if(temp.val != temp.next.val):
    #             temp.val, temp.next.val = temp.next.val, temp.val

    #         temp = temp.next.next

    # def MoveLastElementToFront(self):
    #     prev = None
    #     curr = self.head
    #     while curr.next != None:
    #         prev = curr
    #         curr = curr.next

    #     print(prev.val, curr.val)

    #     prev.next = None
    #     curr.next = self.head
    #     self.head = curr
    #     return

    # def intersection(self, head1, head2):
    #     currX = head1
    #     currY = head2
    #     arr1 = [] 
    #     arr2 = []
    #     arr3 = []
    #     while currX != None:
    #         arr1.append(currX.val)
    #         currX = currX.next

    #     while currY != None:
    #         arr2.append(currY.val)
    #         currY = currY.next

    #     for i in range(len(arr1)):
    #         for j in range(len(arr2)):
    #             if arr1[i] == arr2[j]:
    #                 arr3.append(arr1[i])

    #     print(arr1, arr2, arr3)
    #     link3 = Linked_List()
    #     for i in range(len(arr3)):
    #         link3.append(arr3[i])

    #     return link3.head





# link = Linked_List()
# link.append(1)
# link.append(2)
# link.append(3)
# link.append(4)
# link.append(5)
# link.append(6)
# link.printList(link.head)
# # link.MoveLastElementToFront()
# # link.Swapping('x', 'y')
# # link.printList(link.head)
# # print(link.findinglength())

# link2 = Linked_List()
# link2.append(0)
# link2.append(2)
# link2.append(13)
# link2.append(4)
# link2.append(15)
# link2.append(6)
# link2.printList(link2.head)
# # link2.printList(link2.head)
# # print(link.findinglength())

# head = link.intersection(link.head, link2.head)
# link.printList(head)

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
        head  = self.head
        while head != None:
            print(head.val)
            head = head.next

    def swappingByValue(self, a, b):
        if a==b:
            return 

        head = self.head
        x = None
        y = None
        while head != None:
            if (head.val == a):
                x = head
                head = head.next
            
            if (head.val  == b):
                y = head
                head = head.next
            head = head.next

        if x==y:
            return

        else:
            temp = x.val
            x.val  = y.val
            y.val = temp

    def swapping(self, a, b):
        head = self.head

        currA = self.head
        prevA = None
        while currA.next != None and currA.val != a:
            prevA = currA
            currA = currA.next

        currB = self.head
        prevB = None
        while currB.next != None and currB.val != b:
            prevB = currB
            currB = currB.next
        
        if prevA == None or prevB == None:
            return

        temp = currA.next
        currA.next = currB.next
        currB.next = temp
        temp = prevA.next
        prevA.next = prevB.next
        prevB.next = temp


        return (prevA.val, currA.val, prevB.val, currB.val)


    
    def quicksort(self, start, end):
        if (start == end or start == None or end == None):
            return start

        pivot_pre = start
        curr = start
        pivot = end.val

        while start!=end:
            if(start.val < pivot):
                pivot_pre = curr
                temp = curr.val
                curr.val = start.val
                start.val = temp
                curr = curr.next

            start = start.next

        temp = curr.val
        curr.val = pivot
        end.val = temp

        return pivot_pre

    def sort (self, start, end):
        if(start == None or start == end or start == end.next):
            return

        pivot_prev = self.quicksort(start, end)
        self.sort(start, pivot_prev)

        if(pivot_prev != None and pivot_prev == start):
            self.sort(pivot_prev.next, end)

        elif(pivot_prev != None and pivot_prev.next != None):
            self.sort(pivot_prev.next.next,end)
    

        


link = Linked_List()

link.append(2)
link.append(4)
link.append(1)
link.append(6)
link.append(0) 
link.printList()
link.sort(link.head, link.tail)
print('\n')
link.printList()


