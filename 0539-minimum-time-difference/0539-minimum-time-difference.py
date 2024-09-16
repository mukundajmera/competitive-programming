class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        difference = [value.split(":") for value in timePoints]
        difference = [int(value[0])*60 + int(value[1]) for value in difference]
        difference.sort()
        min_diff = float('inf')
        print(difference)
        for idx in range(1, len(difference)):
            if min_diff > difference[idx] - difference[idx-1]:
                min_diff = difference[idx] - difference[idx-1]
        
        return min(min_diff, 24 * 60 - (difference[-1] - difference[0]))