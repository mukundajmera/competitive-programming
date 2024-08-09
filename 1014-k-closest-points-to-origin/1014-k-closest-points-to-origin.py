class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # points.sort(key = lambda x : x[0] ** 2  + x[1] ** 2)
        # return points[:k]

        heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            dist = -self.squared_distance(points[i])
            if dist > heap[0][0]:
                # If this point is closer than the kth farthest,
                # discard the farthest point and add this one
                heapq.heappushpop(heap, (dist, i))
        
        # print(heap)
        # Return all points stored in the max heap
        return [points[i] for (_, i) in heap]
    
    def squared_distance(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] ** 2