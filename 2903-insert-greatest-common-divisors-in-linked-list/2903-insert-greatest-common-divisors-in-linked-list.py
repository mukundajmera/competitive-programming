# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Helper method to calculate the greatest common divisor using the Euclidean algorithm
        def _calculate_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        # If the list contains only one node, return the head as no insertion is needed
        if not head.next:
            return head

        # Initialize pointers to traverse the list
        node1 = head
        node2 = head.next

        while node2:
            gcd_value = _calculate_gcd(node1.val, node2.val)
            gcd_node = ListNode(gcd_value)

            node1.next = gcd_node
            gcd_node.next = node2

            node1 = node2
            node2 = node2.next

        return head
        
