class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_cite = max(citations)
        counts = [0] * (max_cite + 1)

        for cite in citations:
            counts[cite] += 1
        

        total_paper = 0
        for hidx in range(max_cite, -1, -1):
            total_paper += counts[hidx]
            if total_paper >= hidx:
                return hidx
        
        return 0
