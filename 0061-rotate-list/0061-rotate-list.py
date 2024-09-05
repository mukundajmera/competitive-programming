# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next == None or k <= 0:
            return head
        length = -1
        idx = 0
        curr = head
        while curr:
            idx += 1
            curr = curr.next
        length = idx
        k = k % length
        if k <= 0:
            return head
        idx = length - k
        curr = head
        prev = None
        
        #traverse and find the difference
        while idx > 0:
            idx -= 1
            prev = curr
            curr = curr.next
        #disjoint the list
        old_head = head
        head = curr
        prev.next = None

        #fetch tail 
        while curr and curr.next:
            curr = curr.next

        #join head
        curr.next = old_head
        return head
         