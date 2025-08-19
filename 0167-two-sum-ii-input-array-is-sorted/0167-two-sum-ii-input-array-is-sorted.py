class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            current = numbers[left] + numbers[right]
            if target == current:
                return [ left+1, right+1]
            elif current > target:
                right -=1
            else:
                left += 1
        return [-1, -1]

     # diff = {}
        # result = []
        # if len(numbers) <= 1:
        #     return result
    
        # for idx in range(len(numbers)):
        #     d = target - numbers[idx]
        #     if d in diff:
        #         result.extend( [diff[d] + 1 , idx+1] )
        #         # result.sort()
        #         return result
        #     else:
        #         diff[numbers[idx]] = idx
        # return []