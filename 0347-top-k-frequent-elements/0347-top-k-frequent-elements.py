from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #using hashmap for fetching
        num_freq = Counter(nums)
        heap = []
        for key, value in num_freq.items():
            heapq.heappush(heap, (-value, key))
        
        result = []
        for idx in range(k):
            result.append(heapq.heappop(heap)[1])

        return result            

