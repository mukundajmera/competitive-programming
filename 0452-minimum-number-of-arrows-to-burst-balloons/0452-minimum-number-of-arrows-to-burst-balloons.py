class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])

        current_shot = points[0][1]
        result = 1
        # print(points)
        for idx in range(1, len(points)):
            if points[idx][0] > current_shot:
                result += 1
                current_shot = points[idx][1]
            
        return result