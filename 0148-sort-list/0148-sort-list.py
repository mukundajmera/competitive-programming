# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        current = head

        while current:
            heapq.heappush(heap, current.val)
            current = current.next
        
        current = head

        while current:
            current.val = heapq.heappop(heap)
            current = current.next
        
        return head