# Find nth node from the end of a Linked List


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

def display(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print(None, '\n')

def countLength(head):
    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    return count

# print(countLength(head))

def approach_1(head, index):
    curr = head
    lenghtOfList = countLength(head)
    while curr:
        currLen = countLength(curr)
        if index == currLen:
            return curr
        curr = curr.next


# print(approach_1(head, 2).data)

def approach_2(head, index):
    length = countLength(head)
    if index < 0 or index > length:
        return 'Invalid index'
    
    hashMap = {}
    curr = head
    count = 1
    while curr:
        hashMap[count] = curr.data
        curr = curr.next
        count += 1
    return hashMap[length - index+1]


# print(approach_2(head, 1))
def approach_3(head, index):
    pNext = head
    pTemp = head
    count = 0

    while pTemp:
        count+=1
        if(count == index):
            pNext = pNext.next 
            count = 0
        pTemp = pTemp.next 
    return pNext

def nth_from_end(head, n):
    pNthNode = head
    pTemp = head

    # Move pTemp n nodes ahead
    for _ in range(n):
        if pTemp is None:
            print(f"{n} is greater than the number of nodes in the list.")
            return None
        pTemp = pTemp.next

    # Move both pointers until pTemp reaches the end
    while pTemp:
        pTemp = pTemp.next
        pNthNode = pNthNode.next

    # pNthNode now points to the nth node from the end
    return pNthNode.data

print(nth_from_end(head, 2))
display(head)