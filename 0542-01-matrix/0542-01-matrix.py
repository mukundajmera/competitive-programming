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