class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate_time(rate):
            time = 0
            for idx in range(len(piles)):
                time += (piles[idx] + rate - 1) // rate
            return time

        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            if calculate_time(mid) > h:
                left = mid + 1
            else:
                right = mid
               
        return left