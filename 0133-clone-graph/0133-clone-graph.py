"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #dfs
        if not node:
            return node
        
        if node in self.visited:
            return self.visited[node]
        
        clone = Node(node.val, [])
        self.visited[node] = clone
        if node.neighbors:
            clone.neighbors = [self.cloneGraph(ndx) for ndx in node.neighbors]
        
        return clone
