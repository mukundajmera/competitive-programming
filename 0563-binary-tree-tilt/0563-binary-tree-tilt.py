# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tiles = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal total_tiles
            left_s, right_s = dfs(node.left), dfs(node.right)
            total_tiles += abs(left_s - right_s)
            return left_s + right_s + node.val
        dfs(root)
        return total_tiles