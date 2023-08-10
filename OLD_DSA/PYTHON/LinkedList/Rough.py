import initialisation



        # prev = None
        # curr = head
        # while curr!= None:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # head = prev
        # return head


# class Solution:
#     def reverseList(self, head):
#         prev = None
#         curr = head
#         while curr != None:
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next
#         head = prev
#         return head
    
#     def reverseBetween(self, head, left: int, right: int):

#         curr = head
#         second_last = None
#         while curr != None:
#             if curr.val == left:
#                 second_last = curr
#                 prev = None
#                 while curr.val != right:
#                     print(curr.val)
#                     next = curr.next
#                     curr.next = prev
#                     temp = next.next
#                     prev = curr
#                     curr = temp

#                 head.next = curr
#                 # second_last.next = curr
#             curr = curr.next
#         return head

    # def reverseBetween2(self, head, m: int, n: int):
    #     if not head and m == n:
    #         return head

    #     dummy = ListNode.Node(0)
    #     prev = dummy

    #     for _ in range(m - 1):
    #         prev = prev.next  # Point to the node before the sublist [m, n]

    #     tail = prev.next  # Will be the tail of the sublist [m, n]

    #     # Reverse the sublist [m, n] one by one
    #     for _ in range(n - m):
    #         cache = tail.next
    #         tail.next = cache.next
    #         cache.next = prev.next
    #         prev.next = cache

    #     return dummy.next

    
# s = Solution()
# new_head = s.reverseBetween(link.head, 2, 4)
# print(link.print_list(new_head))

link1 = initialisation.Linked_list()

link1.append(1)
link1.append(2)
link1.append(3)
link1.append(4)
link1.append(5)
link1.append(6)
link1.append(7)
link1.append(8)
# link1.append(9)


link2 = initialisation.Linked_list()
# link2.append(4)
# link2.append(5)
link2.append(6)
link2.append(7)
link2.append(9)

# print(link1.print_list(link1.head))
# print(link2.print_list(link2.head))

link3 = initialisation.Linked_list()
link3.append(1)
link3.append(2)
link3.append(3)
# link3.append(2)
# link3.append(1)
print(link3.print_list(link3.head))



class Solution:
    def mergeTwoLists2(self, list1, list2):
        cur = dummy = initialisation.Node()
        while list1 and list2:               
            if list1.val < list2.val:
                print("if",cur.val, list1.val)
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                print("else",cur.val, list2.val)

                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

    def removeNthFromEnd(self, head, n):
        curr = head
        count = 0
        while curr != None:
            count +=1
            curr = curr.next
        
        if count == n:
            return head.next

        count = count - n
        curr = head

        for i in range(count-1):
            curr = curr.next   

        temp = curr.next.next
        curr.next = temp

        return head

    def addTwoNumbers(self, l1, l2):

        dummy = initialisation.Node(0)
        curr = dummy
        carry = 0

        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            curr.next = initialisation.Node(carry%10)
            carry //= 10
            curr = curr.next
        return dummy.next


    def deleteNode(self, head, node):
        if head.val == node:
            return head.next
        prev = None
        curr = head
        while curr.val != node:
            prev = curr
            curr = curr.next
        temp = curr.next
        prev.next = temp
        return head

    def getIntersectionNode(self, headA, headB):
        # a = headA
        # b = headB
        # while a.val != b.val:
        #     a = a.next if a else headB
        #     b = b.next if b else headA
        # return a

        a = headA
        b = headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a

    def hasCycle(self, head) -> bool:

        s = set()

        curr = head
        while curr:
            if curr in s:
                return True
            
            s.add(curr)
            curr = curr.next

        return False
        
    def reverseKGroup(self, head, k):
        if head == None or k == 1:
            return head

        dummy = initialisation.Node()
        dummy.next = head
        curr = dummy
        nex = dummy
        pre = dummy
        count = 0

        while curr.next != None:
            curr = curr.next
            count+=1

        print("this is COunt", count)

        while count >= k:
            curr = pre.next
            nex = curr.next
            for i in range(k-1):
                curr.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = curr.next
            pre = curr
            count-=k
        return dummy.next

    # def isPalindrome(self, head):
    #     new_arr = []

    #     curr = head
    #     while curr!=None:
    #         new_arr.append(curr.val)
    #         curr = curr.next
        
    #     curr = head
    #     for i in range(len(new_arr)-1 , -1, -1):
    #         if new_arr[i] != curr.val:
    #             return False
    #         curr = curr.next
    #     return True

    def isPalindrome(self, head):
        slow, fast, prev = head, head, None

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None

        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev

        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next

        return True

    def reveseList(self, head):
        pre = None
        next = None
        while head != None:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

    def isPalindrome2(self, head):
        if head == None or head.next == None:
            return head
        
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = self.reveseList(slow.next)
        slow = slow.next

        while slow != None:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next

        return True

    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head

        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        
        t = k % length


        for i in range(t):
            curr = head
            pre = head
            while curr.next != None:
                pre = curr
                curr = curr.next
            pre.next = None
            curr.next = head
            head = curr

        return head

        # [1, 2, 3]
        # 2
        # [3, 1, 2]

        # if not head or not head.next or k == 0:
        #     return head

        # tail = head
        # length = 1
        # while tail.next:
        #     tail = tail.next
        #     length += 1
        # tail.next = head  # Circle the list

        # t = length - k % length
        # print(t)
        # for _ in range(t):
        #     tail = tail.next
        # newHead = tail.next
        # tail.next = None

        # return newHead

        # [2, 3, 1]

    def copyRandomList(self, head):
        if not head:
            return None
        if head in self.map:
            return self.map[head]

        newNode = initialisation.Node(head.val)
        self.map[head] = newNode
        newNode.next = self.copyRandomList(head.next)
        newNode.random = self.copyRandomList(head.random)
        return newNode

    map = {}
            


s = Solution()
print(link1.print_list(s.copyRandomList(link3.head)))

# s.removeNthFromEnd(link1.head, 2)