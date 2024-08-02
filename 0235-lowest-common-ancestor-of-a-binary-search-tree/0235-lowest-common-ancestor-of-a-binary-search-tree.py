# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        lca = None
        def helper(root, p, q):
            nonlocal lca
            if not root:
                return False
            isLeft, isRight = False, False
            if root.left:
                isLeft = helper(root.left, p, q)
            if root.right:
                isRight = helper(root.right, p, q)
            isCurrent = False
            if root == p or root == q:
                isCurrent = True
            if isCurrent + isLeft + isRight >= 2:
                lca = root
            return isCurrent or isLeft or isRight
        helper(root, p, q)
        return lca
            