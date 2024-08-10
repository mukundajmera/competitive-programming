class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        subProblem = [float('inf')] * (amount + 1)
        subProblem[0] = 0

        for coin in coins:
            for num in range(coin, amount+1):
                subProblem[num] = min(subProblem[num], subProblem[num - coin] + 1)

        return -1 if subProblem[amount] == float('inf') else subProblem[amount]