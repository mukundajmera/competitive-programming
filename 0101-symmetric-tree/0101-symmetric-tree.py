# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return helper(root1.left, root2.right) and helper(root1.right, root2.left)
        return helper(root, root)

    # def isMirror(self, r1, r2) -> bool:
    #     if not r1 and not r2:
    #         return True
    #     if not r1 or not r2:
    #         return False

    #     return (r1.val == r2.val) and self.isMirror(r1.left, r2.right) and self.isMirror(r1.right, r2.left)
        
            
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     return self.isMirror(root, root)
