class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        curr_max = -1
        for idx in reversed(range(len(arr))):
            temp_max = arr[idx]
            arr[idx] = curr_max
            curr_max = max(curr_max, temp_max)
        return arr
        
        
        
"""
        n = len(arr)
        max_till_now = arr[-1]
        temp = arr[-1]
        idx = len(arr)-2
        while idx >= 0:
            iter_temp = arr[idx]
            max_till_now = max(temp, max_till_now)
            arr[idx] = max_till_now
            temp = iter_temp
            idx -= 1
        # arr[-2] = arr[-1]
        arr[-1] = -1
        print(arr)
        return arr
"""