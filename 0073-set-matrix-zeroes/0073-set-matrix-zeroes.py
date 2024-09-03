class Solution:
    def helper(self, matrix, row, col, nrow, ncol):        
        #all value of row to zero
        for r in range(ncol):
            self.matrix[row][r] = 0
            
        #all value of col to zero
        for c in range(nrow):
            self.matrix[c][col] = 0
            
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.matrix = matrix
        all_zeros = []
        nrow, ncol = len(matrix), len(matrix[0])
        #fetch all zeros
        for row in range(nrow):
            for col in range(ncol):
                if matrix[row][col] == 0:
                    all_zeros.append((row,col))
        
        
        #iterate for zero value cells and set matrix zeros for other cells
        for row,col in all_zeros:
            self.helper(self.matrix, row, col, nrow, ncol)
        