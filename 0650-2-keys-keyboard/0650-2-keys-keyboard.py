class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            # If d is prime factor, keep dividing
            # n by d until is no longer divisible
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans
        # dp = [float('inf')] * (n + 1)
        # dp[1] = 0
        # for idx in range(2, n+1):
        #     for idj in range(1, (idx // 2) + 1):
        #         if idx % idj == 0:
        #             dp[idx] = min(dp[idx], dp[idj] + (idx// idj))
        # return dp[n]