class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        left, right = 0,  len(intervals)-1
        while left <= right:
            mid = (left + right)//2
            if intervals[mid][0] < newInterval[0]:
                left = mid + 1
            else:
                right = mid - 1
        intervals.insert(left, newInterval)
        result = []
        for inter in intervals:
            if not result or result[-1][1] < inter[0]:
                result.append(inter)
            else:
                result[-1][0] = min(result[-1][0], inter[0])
                result[-1][1] = max(result[-1][1], inter[1])
        return result