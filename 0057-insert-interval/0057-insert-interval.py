class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        #intervals = intervals.sort(key = lambda x : x[0])
        merged = []
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            merged.append(intervals[idx])
            idx += 1
        newValue = []
        # print(merged, "this is before")

        # overlapping interval
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1] :
            newInterval[0] = min(intervals[idx][0], newInterval[0])
            newInterval[1] = max(intervals[idx][1], newInterval[1])
            idx += 1


        merged.append(newInterval)

        # print(merged, "this is after")

        #add remaining
        for rem in range(idx, len(intervals)):
            merged.append(intervals[rem])

        return merged