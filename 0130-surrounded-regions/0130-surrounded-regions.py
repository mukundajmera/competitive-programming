class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        
        rows = len(board)
        cols = len(board[0])
        # recursive function to find all the "O"s that are reachable
        # from the border and mark them as "S"
        def dfs(x, y):
            # return immediately if the cell is out of bounds or is not an "O
            if x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] != 'O':
                return
            board[x][y] = 'S'
            # explore the neighboring cells
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        # initialize the dfs for the first and last column
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)
         # initialize the dfs for the first and last row
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)
        # change the "O"s that are not marked as "S" to "X"s and the "S"s back to "O"s
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
                    
        return board