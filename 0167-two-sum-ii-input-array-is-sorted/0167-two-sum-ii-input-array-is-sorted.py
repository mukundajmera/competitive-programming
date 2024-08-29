class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        diff = {}
        result = []
        if len(numbers) <= 1:
            return result
    
        for idx in range(len(numbers)):
            d = target - numbers[idx]
            if d in diff:
                result.extend( [diff[d] + 1 , idx+1] )
                # result.sort()
                return result
            else:
                diff[numbers[idx]] = idx
        return []
        