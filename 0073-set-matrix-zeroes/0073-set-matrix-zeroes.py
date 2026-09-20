class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrows,ncols = len(matrix), len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        for row in range(nrows):
            for col in range(ncols):

                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in range(nrows):
            for col in range(ncols):

                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0