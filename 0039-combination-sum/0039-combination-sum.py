class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        def dfs(index, stack, current_sum):
            if current_sum == target:
                combinations.append(stack.copy())
                return

            if current_sum > target or index >= len(nums):
                return

            for idx in range(index, len(nums)):
                stack.append(nums[idx])
                dfs(idx, stack, current_sum + nums[idx])
                stack.pop()

            # stack.append(nums[index])
            # dfs(index, stack, current_sum + nums[index])
            # stack.pop()
            # dfs(index + 1, stack, current_sum)
        
        dfs(0, [], 0)
        return combinations