"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        bucket = deque([root])
        while bucket:
            length = len(bucket)
            while length > 0:
                node = bucket.popleft()
                if length == 1:
                    node.next = None
                else:
                    node.next = bucket[0]
                if node.left:
                    bucket.append(node.left)
                if node.right:
                    bucket.append(node.right)
                length -= 1
        return root