class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(arr) + 1)
        for idx in range(len(arr)):
            prefix[idx + 1] = prefix[idx] ^ arr[idx]

        result = [prefix[right + 1] ^ prefix[left] for left, right in queries]
        return result