class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        for idx in range(0, len(s), 2):
            if s[idx] != s[idx+1]:
                changes += 1

        return changes
