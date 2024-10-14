class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = 1
        for idx in range(len(points)):
            p1 = points[idx]
            count = defaultdict(int)
            for idj in range(idx+1, len(points)):
                p2 = points[idj]
                if p2[0] == p1[0]:
                    slope = float('inf')
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                count[slope] += 1
                result = max(result, count[slope] + 1)
        return result