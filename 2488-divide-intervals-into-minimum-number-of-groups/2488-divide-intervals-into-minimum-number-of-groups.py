class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start = sorted(idx[0] for idx in intervals)
        end = sorted(idx[1] for idx in intervals)

        end_idx, group_count = 0, 0

        for index in start:
            if index > end[end_idx]:
                end_idx += 1
            else:
                group_count += 1
        
        return group_count
        # events = []
        # for interval in intervals:
        #     events.append((interval[0], 1))
        #     events.append((interval[1] + 1, -1))
        
        # events.sort(key=lambda event: (event[0], event[1]))

        # max_overlap = 0
        # overlap = 0

        # for event in events:
        #     overlap += event[1]
        
        #     max_overlap = max(max_overlap, overlap)
        
        # return max_overlap