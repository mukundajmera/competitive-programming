# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.list = deque()
        def helper(root) -> list:
            if not root:
                return
            if root.left:
                helper(root.left)
            self.list.append(root.val)
            if root.right:
                helper(root.right)
        helper(root)

    def next(self) -> int:
        if self.list:
            return self.list.popleft()
        else:
            return -1

    def hasNext(self) -> bool:
        if self.list:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()