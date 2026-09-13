# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        queue = deque([root])
        sum_of_level = []
        while queue:
            size = len(queue)
            current_sum = 0
            for _ in range(size):
                node = queue.popleft()
                current_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            sum_of_level.append(current_sum)
        max_value = max(sum_of_level)
        return sum_of_level.index(max_value) + 1