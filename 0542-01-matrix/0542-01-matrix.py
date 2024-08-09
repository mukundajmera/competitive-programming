class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * len(mat[0]) for row in mat]
        nrow, ncol = len(mat), len(mat[0])
        queue = Deque()
        visited = set()
        step = 0
        for row in range(nrow):
            for col in range(ncol):
                if mat[row][col] == 0:
                    queue.append((row,col,step))
                    visited.add((row,col))
        
        directions = [(0,1), (0, -1), (-1, 0), (1, 0)]
        while queue:
            row, col, step = queue.popleft()
            for newr, newc in directions:
                newr += row
                newc += col
                if 0 <= newr < nrow and 0 <= newc < ncol and (newr, newc) not in visited:
                    visited.add((newr,newc))
                    matrix[newr][newc] = step + 1
                    queue.append((newr, newc, step+1))
        return matrix
