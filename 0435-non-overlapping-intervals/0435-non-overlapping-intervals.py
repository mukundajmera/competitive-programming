class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #SORT based on ending
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x[1])
        non_overlapping = 1
        end = intervals[0][1]

        for idx in range(1, len(intervals)):
            #find only non overlapping
            if intervals[idx][0] >= end:
                non_overlapping += 1
                end = intervals[idx][1]

        return len(intervals) - non_overlapping