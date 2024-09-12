class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        double_s = s+s
        substring = double_s[1:-1]
        return s in substring