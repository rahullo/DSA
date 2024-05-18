# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printNode(node):
    curr = node
    while curr != None:
        print(curr.val, "-->", end="")
        curr = curr.next
    print("\n")

class Solution:
    # def mergeTwoLists(self, list1, list2):
        # curr1 = list1
        # curr2 = list2
        # dummy = ListNode()
        # curr = dummy
        # while curr1 != None and curr2 != None:
        #     if curr1.val <= curr2.val:
        #         newNode = ListNode(curr1.val)
        #         curr.next = newNode
        #         curr = curr.next
        #         curr1 = curr1.next
        #     elif curr2.val < curr1.val:
        #         newNode = ListNode(curr2.val)
        #         curr.next = newNode
        #         curr = curr.next
        #         curr2 = curr2.next
        # return dummy.next
    def mergeTwoLists(self, list1, list2):
        if not list1 or not list2:
            return list1 if list1 else list2
        if list1.val > list2.val:
            list1, list2 = list2, list1
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
printNode(l1)
printNode(l2)


s = Solution()

node = s.mergeTwoLists(l1, l2)

printNode(node)