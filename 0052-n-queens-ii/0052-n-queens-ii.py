class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        pos_diag = set() #(r + c)
        neg_diag = set() #(r - c)

        result = 0

        def backtrack(row):
            if row == n:
                nonlocal result
                result += 1
                return
            
            for c in range(n):
                if c in col or (row + c) in pos_diag or (row - c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(row + c)
                neg_diag.add(row - c)
                backtrack(row + 1)
                col.remove(c)
                pos_diag.remove(row + c)
                neg_diag.remove(row - c)
        
        backtrack(0)
        return result

                
                

