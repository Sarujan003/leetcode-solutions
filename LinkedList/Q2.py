# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        # Track the carry-over value
        carry = 0

        # Pointers to traverse the list
        n1 = l1
        n2 = l2

        # Dummy head
        dummy = ListNode(0,None)
        tmp = dummy

        # Iterate until all digits in both lists are processed
        while n1 or n2:
            num1 = 0
            num2 = 0
            if n1:
                num1 = n1.val

            if n2:
                num2 = n2.val

            # Calculate the total sum
            summation = num1 + num2 + carry

            if summation >= 10:
                carry = 1
                summation = summation - 10

            else:
                carry = 0
            
            # Create a new node and make connection
            # exixting node(tmp) ---> null , new node(nxt) ---> null
            nxt = ListNode(summation,None)
            tmp.next = nxt
            tmp = nxt
            # exixting node ---> new node(tmp) ---> null

            if n1:
                n1 = n1.next

            if n2:
                n2 = n2.next

        # append the final node if a carry available
        if carry == 1:
            nxt = ListNode(1,None)
            tmp.next = nxt
            tmp = nxt

        

        return dummy.next
