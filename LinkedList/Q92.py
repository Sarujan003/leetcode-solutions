# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left == right:
            return head

        dummy = ListNode(0,head)
        first = dummy
        pl = dummy.next
        pr = dummy.next

        for i in range(left-1):
            first = pl
            pl = pl.next

        for i in range(right-1):
            pr = pr.next

        last = pr.next

        pr.next = None
        curr, prev = first.next, None

        start = curr

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        first.next = prev
        start.next = last

        return dummy.next

        

        