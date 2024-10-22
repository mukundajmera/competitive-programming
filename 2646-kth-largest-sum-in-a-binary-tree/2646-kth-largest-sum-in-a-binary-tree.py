# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()

        queue.append(root)
        levels = []
        while queue:
            length = len(queue)
            current_level = 0
            for idx in range(length):
                node = queue.popleft()
                current_level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(current_level)
        levels = [-num for num in levels]
        heapq.heapify(levels)
        largest = -1
        if len(levels) < k:
            return -1
        while k > 1:
            k -= 1
            heapq.heappop(levels)

        return -levels[0]