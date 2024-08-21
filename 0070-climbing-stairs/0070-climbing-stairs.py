# Python3
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for idx in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for idx in range(3, n+1):
            dp[idx] = dp[idx - 2] + dp[idx - 1]
        return dp[n]