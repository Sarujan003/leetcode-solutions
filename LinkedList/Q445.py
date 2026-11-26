# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # reverse first list
        # prev1 = None
        # cur = l1

        # while cur:
        #     nxt = cur.next
        #     cur.next = prev1
        #     prev1 = cur
        #     cur = nxt

        # # reverse second list
        # prev2 = None
        # cur = l2

        # while cur:
        #     nxt = cur.next
        #     cur.next = prev2
        #     prev2 = cur
        #     cur = nxt

        # dummy = ListNode(0,None)
        # tmp = dummy

        # carry = 0

        # while prev1 or prev2:
        #     num1 = 0
        #     num2 = 0
        #     if prev1:
        #         num1 = prev1.val

        #     if prev2:
        #         num2 = prev2.val

        #     summation = num1 + num2 + carry

        #     if summation >= 10:
        #         carry = 1
        #         summation = summation - 10
        #     else:
        #         carry = 0

        #     tmp.next = ListNode(summation,None)
        #     tmp = tmp.next

        #     if prev1:
        #         prev1 = prev1.next

        #     if prev2:
        #         prev2 = prev2.next


        # if carry == 1:
        #     tmp.next = ListNode(1,None)

        # # reverse the dummy node
        # prev = None
        # cur = dummy.next

        # while cur:
        #     nxt = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = nxt
            

        # return prev

        stack1 = []
        stack2 = []

        cur = l1

        while cur:
            stack1.append(cur.val)
            cur = cur.next

        cur = l2

        while cur:
            stack2.append(cur.val)
            cur = cur.next

        carry = 0
        dummy = None

        while stack1 or stack2:
            num1 = 0
            num2 = 0
            if stack1:
                num1 = stack1.pop()

            if stack2:
                num2 = stack2.pop()

            summation = num1 + num2 + carry

            if summation >= 10:
                carry = 1
                summation = summation - 10

            else:
                carry = 0

            tmp = ListNode(summation,None)
            tmp.next = dummy
            dummy = tmp

        if carry == 1:
            tmp = ListNode(1,None)
            tmp.next = dummy
            dummy = tmp

            
            

        return dummy
    