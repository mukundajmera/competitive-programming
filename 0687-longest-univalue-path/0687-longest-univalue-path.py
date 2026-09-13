# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_value = 0 
        def dfs(root, parent):
            nonlocal max_value
            if not root:
                return 0

            left = dfs(root.left, root)
            right = dfs(root.right, root)
            max_value = max(max_value, left + right)
            
            return 1 + max(left, right) if root.val == parent.val else 0

        dfs(root, TreeNode(val=0))
        return max_value