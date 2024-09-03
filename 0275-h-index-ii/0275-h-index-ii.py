class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #using BS
        n = len(citations)
        cite = 0
        left, right = 0,  n -1
        while left <= right:
            mid = (left + right)//2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        
        return n - left

        # max_cite = max(citations)
        # counts = [0] * (max_cite + 1)

        # for cite in citations:
        #     counts[cite] += 1
        

        # total_paper = 0
        # for hidx in range(max_cite, -1, -1):
        #     total_paper += counts[hidx]
        #     if total_paper >= hidx:
        #         return hidx
        
        # return 0
