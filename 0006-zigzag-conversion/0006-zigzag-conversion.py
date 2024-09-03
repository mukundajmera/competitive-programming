class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #base case
        if numRows == 1 or len(s) <= numRows:
            return s
        
        idx, adder = 0, 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[idx].append(char)
            if idx == 0:
                adder = 1
            elif idx == numRows-1:
                adder = -1
            
            idx += adder

        for idx in range(numRows):
            rows[idx] = "".join(rows[idx])
        
        return "".join(rows)