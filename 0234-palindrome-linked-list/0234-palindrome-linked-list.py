# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, root):
        if not root:
            return
        prev = None
        curr = root
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return
        #goto half
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #reverse ahead and attach
        slow.next = self.reverse_list(slow.next)
        #goto middle
        slow = slow.next
        curr = head
        isPalindrome = True
        while slow:
            if slow.val != curr.val:
                isPalindrome = False
                break
            curr = curr.next
            slow = slow.next
        return isPalindrome
            