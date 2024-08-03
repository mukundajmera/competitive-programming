# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], height=0) -> int:
        result = [0]
        def helper(root, result):
            if not root:
                return 0            
            left = helper(root.left, result)
            right = helper(root.right, result)
            result[0] = max(result[0], left + right)
            return max(left, right) + 1
        helper(root, result)
        return result[0]