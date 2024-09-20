class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reverse_str = s[::-1]

        for idx in range(len(s)):
            if s[: len(s) - idx] == reverse_str[idx:]:
                return reverse_str[: idx] + s
        return ""