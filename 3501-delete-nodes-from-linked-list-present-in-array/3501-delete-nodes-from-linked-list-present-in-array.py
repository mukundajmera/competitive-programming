# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        values_remove = set(nums)
        while head and head.val in values_remove:
            head = head.next
        
        if not head:
            return None
        
        curr = head
        while curr.next:
            if curr.next.val in values_remove:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
    #     if not head:
    #         return

    #     curr = head
    #     for num in nums:
    #         curr = self.deleteNodes(curr, num)
        
    #     return curr

    # def deleteNodes(self, head, value):
    #     if not head:
    #         return
        
    #     dummy = ListNode(0, head)
    #     prev = dummy
    #     curr = head
    #     while curr:
    #         if curr.val == value:
    #             prev.next = curr.next
    #             curr = curr.next
    #             continue
    #         prev = curr
    #         curr = curr.next
    #     return dummy.next