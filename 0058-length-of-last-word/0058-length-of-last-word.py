class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        return len(s.split()[-1])