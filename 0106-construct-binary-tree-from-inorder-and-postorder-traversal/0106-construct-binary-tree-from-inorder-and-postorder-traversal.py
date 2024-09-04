from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapping = {inorder[idx]: idx for idx in range(len(inorder))}
        postorder = deque(postorder)


        def helper(start, end):
            #base case
            if start > end:
                return None
            
            root = TreeNode(postorder.pop())
            mid = mapping[root.val]

            root.right = helper(mid + 1, end)
            root.left = helper(start, mid - 1)
            return root

        return helper(0, len(postorder) - 1)


        # idx_map = {val: idx for idx, val in enumerate(inorder)}
        # def helper(left, right) -> TreeNode:
        #     if left > right:
        #         return None
            
        #     val = postorder.pop()
        #     root = TreeNode(val)
        #     idx = idx_map[val]

        #     root.right = helper(idx+1, right)
        #     root.left = helper(left, idx-1)
        #     return root
        # return helper(0, len(inorder)-1)