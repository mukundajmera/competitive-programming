# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        left2right = True
        result = []
        while queue:
            length = len(queue)
            node_level = deque()
            for _ in range(length):
                node = queue.popleft()

                if left2right:
                    node_level.append(node.val)
                else:
                    node_level.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(node_level))
            left2right = not left2right
        return result

        # queue = deque()
        # output = []
        
        # if not root:
        #     return output
        
        # queue.append(root)
        # ltr = True
        # while queue:
        #     current = []
        #     stack = []
        #     while queue:
        #         element = queue.popleft()
        #         if element.left:
        #             stack.append(element.left)
        #         if element.right:
        #             stack.append(element.right)
        #         current.append(element.val)
        #     if ltr:
        #         output.append(current)
        #         ltr = False
        #     else:
        #         output.append(current[::-1])
        #         ltr = True
        #     # print(current, stack, ltr)
        #     queue.extend(stack)
        # return output
