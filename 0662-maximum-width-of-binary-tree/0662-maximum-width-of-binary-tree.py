# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 0)])
        max_value = 0
        while queue:
            size = len(queue)
            _, leftPos = queue[0]
            rightPos = -1
            for idx in range(size):
                node, pos = queue.popleft()

                if idx == size - 1:
                    rightPos = pos

                if node.left:
                    queue.append((node.left, 2 * pos + 1))

                if node.right:
                    queue.append((node.right, 2 * pos + 2))
            
            max_value = max(max_value, rightPos - leftPos + 1)
        return max_value