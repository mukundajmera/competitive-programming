class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            distance = abs(num - x)
            if len(heap) < k:
                heapq.heappush(heap, (-distance, num))
            elif distance < -heap[0][0]:
                heapq.heappushpop(heap, (-distance, num))
        
        distances = [pair[1] for pair in heap]
        distances.sort()
        return distances

        # left = 0
        # right = len(arr) - k
        
        # # Binary search against the criteria described
        # while left < right:
        #     mid = (left + right) // 2
        #     if x - arr[mid] > arr[mid + k] - x:
        #         left = mid + 1
        #     else:
        #         right = mid

        # return arr[left:left + k]