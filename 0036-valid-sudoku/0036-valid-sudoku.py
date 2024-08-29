class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                #main logic
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row // 3, col // 3)]:
                    return False
                
                board_value = board[row][col]
                cols[col].add(board_value)
                rows[row].add(board_value)
                squares[(row // 3, col // 3)].add(board_value)
        
        return True


