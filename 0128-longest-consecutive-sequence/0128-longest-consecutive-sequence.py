class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        for num in nums:
            #find the smallest for that sequence
            if(num-1) not in num_set:
                length = 0
                #find all values till it exist
                while (num + length) in num_set:
                    length += 1
                count = max(count, length)
        return count