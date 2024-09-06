# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head, k):
        prev = None
        curr = head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev, curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        dummy = ListNode(0, head)
        ptr = dummy
        while ptr:
            track = ptr
            for idx in range(k):
                track = track.next
                #edge case
                if not track:
                    return dummy.next
            prev, curr = self.reverseList(ptr.next, k)
            #save node
            lastNode = ptr.next
            #next ahead group
            lastNode.next = curr
            ptr.next = prev
            #jump
            ptr = lastNode
        
        return dummy.next

    