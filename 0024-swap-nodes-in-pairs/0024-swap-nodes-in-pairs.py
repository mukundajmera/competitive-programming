# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        first = head

        while first and first.next:
            second = first.next
            _next = second.next
            #swap
            prev.next = second
            second.next = first
            first.next = _next
            prev = first
            first = _next

        return dummy.next