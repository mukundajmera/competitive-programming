# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        total = 0
        curr = head
        while curr:
            total += 1
            curr = curr.next
        total -= n
        if total == 0:
            return head.next
        prev = head
        curr = head
        while total > 0:
            prev = curr
            curr = curr.next
            total -= 1
        prev.next = curr.next
        return head
    