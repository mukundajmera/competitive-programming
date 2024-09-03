class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowLen=len(board)
        colLen=len(board[0])
        ans = [[-1 for x in range(colLen)] for y in range(rowLen)]
        def inBound(r,c):
            return (0<=r<rowLen) and (0<=c<colLen)

        for row in range(rowLen):
            for col in range(colLen):
                count = 0

                for r, c in  [(row,col+1),(row,col-1),(row-1,col),(row+1,col),(row-1,col+1),(row+1,col-1),(row+1,col+1),(row-1,col-1)]:
                    if inBound(r,c):
                        print((row,col), (r,c))
                        count += board[r][c]

                if count<2:
                    ans[row][col]=0
                elif board[row][col]==1 and (count==2 or count==3):
                    ans[row][col]=1
                elif board[row][col]==1 and count>3:
                    ans[row][col]=0
                elif board[row][col]==0 and count==3:
                    ans[row][col]=1
                else:
                    ans[row][col]=board[row][col]
                
        board[:] = ans
        return board