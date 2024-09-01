class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        result = [[0] * n for _ in range(m)]
        index = 0
        for idx in range(m):
            result[index] = original[(idx*n):(idx + 1) * n]
            index += 1
        return result