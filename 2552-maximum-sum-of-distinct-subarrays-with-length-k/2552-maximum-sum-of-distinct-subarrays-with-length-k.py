class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = float("-inf")
        state = {}
        current_sum = 0
        start = 0
        for end in range(len(nums)):
            current_sum += nums[end]
            state[nums[end]] = state.get(nums[end], 0) + 1

            if end - start + 1 == k:
                if len(state) == k:
                    max_sum = max(max_sum, current_sum)
                
                current_sum -= nums[start]
                state[nums[start]] -= 1
                if state[nums[start]] == 0:
                    del state[nums[start]]
                start += 1
        
        return 0 if max_sum == float("-inf") else max_sum

        # max_sum = float('-inf')
        # state = 0
        # start = 0
        
        # for end in range(len(nums)):
        #     state += nums[end]
        #     if end - start + 1 == k:
        #         max_sum = max(max_sum, state)
        #         state -= nums[start]
        #         start += 1
        # return max_sum