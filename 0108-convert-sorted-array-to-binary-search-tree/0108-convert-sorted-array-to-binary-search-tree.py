# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        if length == 0:
            return
        mid = TreeNode( nums[length//2] )
        mid.left = self.sortedArrayToBST(nums[:length//2])
        mid.right = self.sortedArrayToBST(nums[(length//2)+1:])
        return mid

    # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    #     l = len(nums)
    #     if l == 0:
    #         return None
    #     curNode = TreeNode(nums[l//2])
    #     curNode.left = self.sortedArrayToBST(nums[0:l//2])
    #     curNode.right = self.sortedArrayToBST(nums[l//2+1:])
    #     return curNode
