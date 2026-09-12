# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_, max_):
            # base case
            if node is None:
                return True
            # check if the current node's value is within the valid range
            if node.val <= min_ or node.val >= max_:
                return False
            return dfs(node.left, min_, node.val) and dfs(node.right, node.val, max_)
        return dfs(root, float('-inf'), float('inf'))

        # def dfs(node, max_val, min_val):
        #     if not node:
        #         return True
            
        #     is_valid = False
        #     if min_val < node.val < max_val:
        #         is_valid = True
            
        #     return is_valid and dfs(node.left, node.val, min_val) and dfs(node.right, max_val, node.val)
        
        # return dfs(root,  float('inf'), float('-inf'))   