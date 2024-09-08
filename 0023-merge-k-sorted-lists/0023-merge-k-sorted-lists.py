# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #using heap appraoch
        heap = []
        for list_idx in lists:
            curr = list_idx
            while curr:
                heap.append(curr.val)
                curr = curr.next

        
        heapq.heapify(heap)

        dummy = ListNode(0)
        prev = dummy
        while heap:
            prev.next = ListNode(heapq.heappop(heap))
            prev = prev.next
        
        return dummy.next