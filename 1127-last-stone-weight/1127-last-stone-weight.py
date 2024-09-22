class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-num for num in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1, stone2 = -heapq.heappop(stones), -heapq.heappop(stones)
            if (diff:= abs(stone1 - stone2)) != 0:
                heapq.heappush(stones,-diff)
        
        return -stones[0] if len(stones) == 1 else 0