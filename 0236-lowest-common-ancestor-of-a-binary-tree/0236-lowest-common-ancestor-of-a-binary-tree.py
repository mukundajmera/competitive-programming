# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        def dfs(root):
            nonlocal lca 
            if not root:
                return False
            
            isLeft = dfs(root.left)
            isRight = dfs(root.right)
            
            isRoot = False
            if root == p or root == q:
                isRoot = True
            
            if isLeft + isRoot + isRight >= 2:
                lca = root

            return isRoot or isLeft or isRight
        dfs(root)
        return lca
