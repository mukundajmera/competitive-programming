class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for idx in range(len(points)):
            x, y = points[idx]
            distance = x ** 2 + y ** 2
            
            if len(heap) < k:
                heapq.heappush(heap, (-distance, idx))
            elif distance < -heap[0][0]:
                heapq.heappushpop(heap, (-distance, idx))
        
        return [points[p[1]] for p in heap]