# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0,head)
        left = dummy.next
        right = head

        if not head or not head.next:
            return dummy.next

        length, tail = 1, head

        while tail.next:
            tail = tail.next
            length += 1

        k = k % length

        if k == 0:
            return dummy.next

        for i in range(k):
            if right.next:
                right = right.next
            else:
                right = head

        while right.next:
            left = left.next
            right = right.next

        tmp = left.next
        left.next = None
        right.next = dummy.next
        dummy.next = tmp

        return dummy.next
