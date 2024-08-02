# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return True, -1
        leftB, leftH = self.helper(root.left)
        rightB, rightH = self.helper(root.right)
        if not leftB or not rightB or abs(leftH - rightH) > 1:
            return False, 0
                
        return True, 1 + max(leftH, rightH)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
        return self.helper(root)[0]