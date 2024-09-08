class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nlen, mlen = len(nums1), len(nums2)
        answer = []
        visited = set()
        min_heap = []
        pairs = []
        for idx in range(min(k, nlen)):
            heapq.heappush(min_heap, (nums1[idx] + nums2[0], idx, 0))
        
        counter = 1

        while min_heap and counter <= k:
            sum_of_pair, p1, p2 = heapq.heappop(min_heap)
            pairs.append([nums1[p1], nums2[p2]])

            next_element = p2 +1

            if len(nums2) > next_element:
                heapq.heappush(min_heap, (nums1[p1] + nums2[next_element], p1, next_element))
            
            counter += 1
        
        return pairs