# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        output = []
        if root.left:
            output.extend(self.postorderTraversal(root.left))
        if root.right:
            output.extend(self.postorderTraversal(root.right))
        output.append(root.val)
        return output