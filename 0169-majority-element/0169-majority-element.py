class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = -1
        for num in nums:
            if num == majority:
                count += 1
                continue
            if count == 0:
                majority = num
                count = 1
            count -= 1
        return majority
    # def majorityElement(self, nums: List[int]) -> int:
    #     numbers = Counter(nums)
    #     for key,value in numbers.items():
    #         if value > len(nums) // 2:
    #             return key
    #     return result