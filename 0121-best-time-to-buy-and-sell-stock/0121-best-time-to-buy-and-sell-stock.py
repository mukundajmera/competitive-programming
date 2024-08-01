class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyAt = prices[0]
        profit = 0
        for price in range(1, len(prices)):
            if buyAt > prices[price]:
                buyAt = prices[price]
            profit = max(profit, prices[price] - buyAt)
        return profit