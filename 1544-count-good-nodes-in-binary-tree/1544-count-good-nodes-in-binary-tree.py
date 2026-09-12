# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, current_max):
            if not node:
                return 0
            
            count = 0
            if node.val >= current_max:
                count += 1
                current_max = node.val
            
            return count + dfs(node.left, current_max) + dfs(node.right, current_max)

        
        return dfs(root, root.val)