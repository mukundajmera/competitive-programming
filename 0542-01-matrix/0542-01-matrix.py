class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        nrow, ncol = len(mat), len(mat[0])
        output = [[-1]*ncol for _ in range(nrow)]
        input_arr = []
        for row in range(nrow):
            for col in range(ncol):
                if mat[row][col] == 0:
                    input_arr.append((row,col))
                    output[row][col] = 0
        queue = deque(input_arr)
        distance = 1
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for nr, nc in direction:
                    nr = nr + row
                    nc = nc + col
                    if 0 <= nr < nrow and 0 <= nc < ncol and output[nr][nc] == -1:
                        output[nr][nc] = distance
                        queue.append((nr, nc))
            distance += 1
        return output

        # matrix = [[0] * len(mat[0]) for row in mat]
        # nrow, ncol = len(mat), len(mat[0])
        # queue = Deque()
        # visited = set()
        # step = 0
        # for row in range(nrow):
        #     for col in range(ncol):
        #         if mat[row][col] == 0:
        #             queue.append((row,col,step))
        #             visited.add((row,col))
        
        # directions = [(0,1), (0, -1), (-1, 0), (1, 0)]
        # while queue:
        #     row, col, step = queue.popleft()
        #     for newr, newc in directions:
        #         newr += row
        #         newc += col
        #         if 0 <= newr < nrow and 0 <= newc < ncol and (newr, newc) not in visited:
        #             visited.add((newr,newc))
        #             matrix[newr][newc] = step + 1
        #             queue.append((newr, newc, step+1))
        # return matrix