# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(0), ListNode(0)
        lptr, rptr = left, right

        while head:
            if head.val < x:
                lptr.next = head
                lptr = lptr.next
            else:
                rptr.next = head
                rptr = rptr.next

            temp = head.next
            head.next = None
            head = temp
        
        lptr.next = right.next
        return left.next