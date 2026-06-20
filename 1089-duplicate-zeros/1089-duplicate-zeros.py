class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        end = len(arr) - 1
        last_zero = -1
        for i, n in enumerate(arr):
            if i >= end:
                break
            if n == 0:
                last_zero = i
                end -= 1
        ptr = len(arr) - 1
        print(end,ptr)
        for i in range(end, -1, -1):
            arr[ptr] = arr[i]
            ptr -= 1
            if arr[i] == 0 and i <= last_zero:
                arr[ptr] = 0
                ptr -= 1
