class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrow, ncol = len(matrix), len(matrix[0])

        #take transpose
        for row in range(nrow):
            for col in range(row, ncol):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        #reverse it
        for row in range(nrow):
            matrix[row] = matrix[row][::-1]    