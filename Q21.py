# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        output = dummy
        while (list1 != None) and (list2 != None):
            if list1.val <= list2.val:
                output.next = list1
                list1 = list1.next
            else:
                output.next = list2
                list2 = list2.next

            output = output.next
        
        if (list2 != None):
            output.next = list2

        if (list1 != None):
            output.next = list1


        # arrayList = []
        # current = output
        # while current != None:
        #     arrayList.append(current.val)
        #     current = current.next

        return dummy.next



        