# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = -inf
        def check(node):
            nonlocal ans
            if not node:
                return 0
            l = max(0, check(node.left))
            r = max(0, check(node.right))
            ans = max(ans, l + node.val + r)
            return node.val + max(l, r)
        check(root)
        return ans