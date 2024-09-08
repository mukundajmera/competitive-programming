# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, current_min, current_max):
            if not root:
                return True
            
            return current_min < root.val < current_max and dfs(root.left, current_min, root.val) and dfs(root.right, root.val, current_max)
            
        return dfs(root, -float('inf'), float('inf'))