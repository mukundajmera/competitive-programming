# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2

        dummy = ListNode(0)
        prev = dummy

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                prev.next = ptr1
                ptr1 = ptr1.next
            else:
                prev.next = ptr2
                ptr2 = ptr2.next
            prev = prev.next

        if ptr1:
            prev.next = ptr1
        else:
            prev.next = ptr2

        return dummy.next