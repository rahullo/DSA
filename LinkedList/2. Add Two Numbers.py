# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        a1 = l1.val if l1 else 0
        a2 = l2.val if l2 else 0

        sum = a1 + a2 + carry
        carry = sum // 10
        sum = sum % 10

        curr.next = ListNode(sum)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next



l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

ans = addTwoNumbers(l1, l2)

while ans:
    print(ans.val, " -> ", end='')
    ans = ans.next