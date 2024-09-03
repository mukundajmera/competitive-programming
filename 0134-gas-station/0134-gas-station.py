class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_of_gas = sum(gas)
        sum_of_cost = sum(cost)
        if sum_of_cost > sum_of_gas:
            return -1

        current = 0
        start = 0
        for idx in range(len(gas)):
            current += gas[idx] - cost[idx]
            if current < 0:
                current = 0
                start = idx + 1
        return start