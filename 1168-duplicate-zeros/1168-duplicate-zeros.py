class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = 0
        n = len(arr)
        while idx < n:            
            if arr[idx] == 0 and idx != n-1:
                stop = idx + 1
                itr = n-1
                while stop < itr:
                    arr[itr] = arr[itr-1]
                    itr -= 1
                arr[stop] = 0
                idx += 1
            idx += 1

        