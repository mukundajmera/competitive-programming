class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_num, min_num = arrays[0][-1], arrays[0][0]
        max_dist = 0
        for idx in range(1,len(arrays)):
            max_dist = max(max_dist, abs(arrays[idx][-1] - min_num), abs(max_num - arrays[idx][0]) )
            min_num = min(min_num, arrays[idx][0])
            max_num = max(max_num, arrays[idx][-1])
        
        return max_dist