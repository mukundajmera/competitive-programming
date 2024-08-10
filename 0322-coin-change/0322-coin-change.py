class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        subProblem = [float('inf')] * (amount + 1)
        subProblem[0] = 0

        for num in range(1, amount + 1):
            for coin in coins:
                if num - coin >= 0:
                    subProblem[num] = min(subProblem[num], 1 + subProblem[num - coin])

        return -1 if subProblem[amount] == float('inf') else subProblem[amount]