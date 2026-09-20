class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray = 0
        count = 0
        prefix_count = {0:1}
        sum_ = 0

        for num in nums:
            sum_ += num
            
            if sum_ - k in prefix_count:
                subarray += 1
                count += prefix_count[sum_ - k]
            prefix_count[sum_] = prefix_count.get(sum_, 0) + 1

        return count