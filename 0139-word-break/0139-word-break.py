class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for idx in range(len(s)):
            for word in wordDict:
                if idx < len(word) - 1:
                    continue

                if idx == len(word) - 1 or dp[idx - len(word)]:
                    if s[idx - len(word) + 1: idx + 1] == word:
                        dp[idx] = True
                        break
        # print(dp)
        return dp[-1]