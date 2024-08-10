class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #using left and right prefix sum
        answer = [1] * len(nums)

        #compute left
        current_sum = 1
        for idx in range(len(nums)):
            answer[idx] *= current_sum
            current_sum *= nums[idx]
        
        #compute right
        current_sum = 1
        for idx in reversed(range(len(nums))):
            answer[idx] *= current_sum
            current_sum *= nums[idx]

        return answer
        