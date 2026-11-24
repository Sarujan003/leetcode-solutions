# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy
        left = dummy.next
        right = dummy.next

        if not head:
            return dummy.next

        if head.next:
            right = right.next

        else:
            return dummy.next

        while left and right:
            tmp = right.next
            left.next = right.next
            right.next = left

            prev.next = right
            prev = left

            left = tmp

            if tmp:
                right = left.next

            else:
                right = None

        return dummy.next
            