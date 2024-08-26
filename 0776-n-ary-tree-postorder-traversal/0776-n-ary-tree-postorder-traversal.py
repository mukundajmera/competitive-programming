"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result
        
        stack = [root]
        while stack:
            current = stack.pop()
            result.append(current.val)
            for child in current.children:
                stack.append(child)
        result.reverse()
        return result