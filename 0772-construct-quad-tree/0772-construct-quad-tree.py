"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        nrow = len(grid)
        ncol = len(grid[0])
        return self.create_tree(grid, 0, nrow, 0, ncol)

    def create_tree(self, grid, si, ei, sj, ej):
        val = grid[si][sj]
        node = Node(val == 1, True)
        for row in range(si, ei):
            for col in range(sj, ej):
                if grid[row][col] != val:
                    node.isLeaf = False
                    midI = (si + ei) // 2
                    midJ = (sj + ej) // 2

                    node.topLeft = self.create_tree(grid, si, midI, sj, midJ)
                    node.topRight = self.create_tree(grid, si, midI, midJ, ej)
                    node.bottomLeft = self.create_tree(grid, midI, ei, sj, midJ)
                    node.bottomRight = self.create_tree(grid, midI, ei, midJ, ej)
                    return node
        
        node.isLeaf = True
        node.topLeft = None
        node.topRight = None
        node.bottomLeft = None
        node.bottomRight = None

        return node
