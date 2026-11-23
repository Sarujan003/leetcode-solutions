# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next:
            return True
        
        # 1. Find the end of the first half
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        second = slow.next
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 3. Compare both halves
        first, second = head, prev

        while second:
            if first.val != second.val:
                return False

            second = second.next
            first = first.next

        return True