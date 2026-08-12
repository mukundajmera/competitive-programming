# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        split = slow.next
        slow.next = None

        #Reverse  the second half
        prev = None
        while split:
            _next = split.next
            split.next = prev
            prev = split
            split = _next
        
        split = prev

        final_head = head
        while split:
            part1  = final_head.next
            part2 = split.next

            final_head.next = split
            split.next = part1

            final_head = part1
            split = part2
    
        