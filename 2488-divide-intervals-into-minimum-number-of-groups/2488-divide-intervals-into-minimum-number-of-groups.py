class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for interval in intervals:
            events.append((interval[0], 1))
            events.append((interval[1] + 1, -1))
        
        events.sort(key=lambda event: (event[0], event[1]))

        max_overlap = 0
        overlap = 0

        for event in events:
            overlap += event[1]
        
            max_overlap = max(max_overlap, overlap)
        
        return max_overlap