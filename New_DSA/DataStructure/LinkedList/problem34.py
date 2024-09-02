# Reverse the linked list in pairs. If you have a linked list that holds 1
# →2→3→4→X, then after the function has been called the linked list would hold 2→ 1→4
# →3→X.

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
# head.next.next.next.next.next = Node(6)

def display(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print(None, '\n')

def reversePair(head):
    temp1 = None
    temp2 = None

    while head!=None and head.next != None:
        if temp1 != None:
            temp1.next.next = head.next 
        temp1 = head.next 
        head.next = head.next.next 
        temp1.next = head
        if(temp2 == None):
            temp2 = temp1 
        head = head.next 

    return temp2

def reversePairRecursive(head):
    if head == None or head.next == None:
        return
    else:
        temp = head.next 
        head.next = temp.next 
        temp.next = head
        head = temp

        head.next.next = reversePairRecursive(head.next.next)
        return head
    
def reverse_in_pairs(head):
    if not head or not head.next:
        return head
    
    # Initialize the pointers
    prev = None
    current = head

    # Update head to the second node, which will become the new head
    head = current.next

    while current and current.next:
        next_pair = current.next.next
        second = current.next
        
        # Reverse the current pair
        second.next = current
        current.next = next_pair
        
        # # Link the previous pair with the current reversed pair
        if prev:
            prev.next = second
        
        # Update prev and current for the next iteration
        prev = current
        current = next_pair
    return head
    
display(head)
# display(reversePairRecursive(head))
# display(reversePair(head))
display(reverse_in_pairs(head))
# display(head)


