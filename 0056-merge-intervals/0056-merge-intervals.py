class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        for interval in intervals:
            if not result or (result[-1][1] < interval[0] or interval[1] < result[-1][0]):
                result.append(interval)
            else:
                result[-1][0] = min(result[-1][0], interval[0])
                result[-1][1] = max(result[-1][1], interval[1])
        return result
            
