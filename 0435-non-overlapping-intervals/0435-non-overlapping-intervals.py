class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval : interval[1])
        count = 0
        prev = intervals[0]
        print(intervals)
        for idx in range(1,len(intervals)):
            start, end = intervals[idx][0], intervals[idx][1]
            if prev[1] > start:
                # print(start,end)
                count += 1
                continue
            prev = intervals[idx]
        return count