
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Linked_List:
#     def __init__(self):
#         self.head = None
#         self.tail = self.head
#         self.length = 0

#     def append(self, data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#             self.tail = self.head
#             self.length = 1
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#             self.length+=1

#     def prepend(self, data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#             self.tail = self.head
#             self.length = 1
#         else:
#             new_node.next = self.head
#             self.head = new_node
#             self.length+=1


#     def insert(self, index, data):
#         if index == 1:
#             return self.prepend(data)
            
#         if index >= self.length:
#             return self.append(data)

#         current_node = self.head
#         new_node = Node(data)
#         for i in range(index-1):
#             leader = current_node
#             current_node = current_node.next

#         leader.next = new_node
#         new_node.next = current_node
#         self.length+=1


#     def delete(self, data):
#         current_node = self.head
#         if current_node == None:
#             print('Linked list is Empty.')
#             return

#         elif current_node.data == data:
#             self.head = current_node.next
#             self.length-=1
#             return
        
#         for i in range(self.length):
#             leader = current_node
#             current_node = current_node.next
#             if current_node == None:
#                 return "Not Found"
#             elif current_node.data == data:
#                 leader.next = current_node.next
#                 self.length-=1
        

#     def print_list(self):
#         if self.head == None:
#             print("Empty")
#         else:
#             current_node = self.head
#             while current_node!= None:
#                 print(current_node.data, end= ' ')
#                 current_node = current_node.next
        

# list1 = Linked_List()
# list1.prepend(2)
# list1.append(3)
# list1.append(4)
# list1.append(5)
# list1.insert(1, 1)
# list1.delete(1)
# print(list1.print_list())
# print(list1.length)




class Node:
    def __init__(self,val=0, next=None, random = None):
        self.val = val
        self.next = None
        self.random = random

class Linked_list():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def print_list(self, head):
        array = []
        if head == None:
            return "Sorry!!! Your linked list is Empty"
        else:
            current_node  = head
            while current_node != None:
                array.append(current_node.val)
                current_node = current_node.next

            return array

    def append(self, val):
        new_node = Node(val)
        if self.head ==None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length+=1

    def prepend(self, val):
        new_node = Node(val)
        if self.head ==None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length +=1

    def insert(self, index, val):
        new_node = Node(val)
        if index <=1:
            self.prepend(val)
        elif index >= self.length:
            self.append(val)
        else:
            current_node = self.head
            previous_node = current_node
            for i in range(index-1):
                previous_node = current_node
                current_node = current_node.next
            
            previous_node.next = new_node
            new_node.next = current_node
            self.length += 1

    def delete_by_value(self, value):
        if self.head == None:
            print("Sorry!! Linked list is already Empty.")
            return
        
        if self.head.val == value:
            self.head = self.head.next
            self.length -= 1
            return
        else:
            current_node = self.head
            for i in range(self.length-1):
                previous_node = current_node
                current_node = current_node.next
                if current_node.val == value:
                    previous_node.next = current_node.next
                    self.length-=1
                
    



link = Linked_list()
link.append(3)
link.append(4)
link.append(5)
link.prepend(2)
link.prepend(0)
link.insert(2, 1)
link.insert(1, -1)
link.insert(8, 6)
# link.delete(8)
# link.delete_by_value(5)
# link.delete_by_value(4)
# link.delete_by_value(-1)

# print(link.print_list())
# print(link.length)