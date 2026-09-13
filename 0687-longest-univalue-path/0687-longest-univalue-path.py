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
        # max_value = 0

        # def dfs(node):
        #     if not node:
        #         return 0
        #     nonlocal max_value
            
        #     left_length = dfs(node.left)
        #     right_length = dfs(node.right)
        #     left_arrow = right_arrow = 0

        #     # check if children have the same value as the current node,
        #     # which means we can extend the univalue path by including the
        #     # current node
        #     if node.left and node.left.val == node.val:
        #         left_arrow = left_length + 1
        #     if node.right and node.right.val == node.val:
        #         right_arrow = right_length + 1

        #     max_value = max(max_value, left_arrow + right_arrow)
        #     return max(left_arrow, right_arrow)
            
        # dfs(root)
        # return max_value