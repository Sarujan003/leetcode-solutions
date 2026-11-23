# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(inf,None)
        current = dummy

        while head != None:
            if current.val == head.val:
                head = head.next
                continue
            current.next = head
            head = head.next
            current = current.next

        current.next = None

        return dummy.next