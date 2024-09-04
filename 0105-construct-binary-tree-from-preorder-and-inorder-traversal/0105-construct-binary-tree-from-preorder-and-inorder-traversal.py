from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        mapping = {inorder[idx]: idx for idx in range(len(inorder))}
        preorder = deque(preorder)


        def helper(start, end):
            #base case
            if start > end:
                return None
            
            root = TreeNode(preorder.popleft())
            mid = mapping[root.val]

            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)

            return root

        return helper(0, len(preorder) - 1)

        
        # idx_map = {val: idx for idx, val in enumerate(inorder)}
        
        # def helper(left, right) -> TreeNode:
        #     nonlocal preorder_index
        #     if left > right:
        #         return None
            
        #     val = preorder[preorder_index]
        #     preorder_index += 1

        #     root = TreeNode(val)
        #     idx = idx_map[val]
            
        #     root.left = helper(left, idx - 1)
        #     root.right = helper(idx + 1, right)

        #     return root
        # preorder_index = 0
        # return helper(0, len(inorder)-1)