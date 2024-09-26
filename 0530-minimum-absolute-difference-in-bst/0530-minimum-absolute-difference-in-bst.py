# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    answer = float('inf')

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return

            helper(root.left)
            if self.prev:
                self.answer = min(self.answer, abs(root.val - self.prev.val))
            
            self.prev = root
            helper(root.right)
        
        helper(root)
        return self.answer
