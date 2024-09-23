class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = []

        def binary_search(result, num):
            left, right = 0, len(result) - 1

            while left <= right:
                mid = (left + right)//2

                if result[mid] == num:
                    return mid
                elif result[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1                
            return left

        for num in nums:
            if not result or result[-1] < num:
                result.append(num)
            else:
                idx = binary_search(result, num)
                result[idx] = num
        
        return len(result)