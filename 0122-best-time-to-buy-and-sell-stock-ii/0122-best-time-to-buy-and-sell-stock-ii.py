class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        start = prices[0]
        for idx in range(len(prices)):
            if start < prices[idx]:
                max_profit += prices[idx] - start
            
            start = prices[idx]
        return max_profit

        return max_profit