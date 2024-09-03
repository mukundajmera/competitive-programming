class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrow, ncol = len(matrix), len(matrix[0])
        #transpose for matrix
        for row in range(nrow):
            for col in range(row, ncol):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        #reverse the matrix
        for row in range(nrow):
            matrix[row][:] = matrix[row][::-1]
        
        
