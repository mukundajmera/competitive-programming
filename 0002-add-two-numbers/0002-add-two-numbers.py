# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return
        result = None
        curr = None
        p1, p2 = l1, l2
        carry = False
        while p1 or p2:
            sum = 0
            if p1:
                sum += p1.val
                p1 = p1.next
            if p2:
                sum += p2.val
                p2 = p2.next

            if carry:
                sum += 1
                carry = False

            digit = sum%10
            
            if sum >= 10:
                carry = True
            node = ListNode(digit)
            if not result:
                result = node
                curr = result
            else:
                curr.next = node
                curr = curr.next

        if carry:
            curr.next = ListNode(1)
        return result
            