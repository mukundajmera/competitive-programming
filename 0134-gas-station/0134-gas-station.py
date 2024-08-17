class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_of_gas = sum(gas)
        sum_of_cost = sum(cost)
        if sum_of_cost > sum_of_gas:
            return -1
        
        current_gas, start = 0 ,0 
        for idx in range(len(gas)):
            current_gas += gas[idx] - cost[idx]
            if current_gas < 0:
                current_gas = 0
                start = idx + 1
        return start