class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        left, right = 0, 1
        window = set([s[left]])
        max_size = len(window)
        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                right += 1
            elif s[right] in window:
                while left < right and s[left] != s[right]:
                    window.remove(s[left])
                    left += 1
                left += 1
                right += 1                
            max_size = max(max_size, len(window))
        return max_size