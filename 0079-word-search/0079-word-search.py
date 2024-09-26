class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])
        visited = [[False]* cols for _ in range(rows)]

        def backtrack(r, c, index):
            if index == len(word):
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or board[r][c] != word[index]:
                return False
            
            visited[r][c] = True

            # Explore all four directions: down, up, right, left
            found = (backtrack(r + 1, c, index + 1) or
                     backtrack(r - 1, c, index + 1) or
                     backtrack(r, c + 1, index + 1) or
                     backtrack(r, c - 1, index + 1))
            
            visited[r][c] = False
            return found
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False