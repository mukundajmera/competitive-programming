class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count_close, count_open = 0, 0
        for ch in s:
            if ch == "(":
                count_open += 1
            else:
                if count_open > 0:
                    count_open -= 1
                else:
                    count_close += 1
        
        return count_close + count_open
    