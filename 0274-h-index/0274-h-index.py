class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counts = [0] * (n + 1)
        for cite in citations:
            cite_idx = min(cite, n)
            counts[cite_idx] += 1
        
        hidx = n
        papers = counts[n]
        while papers < hidx:
            hidx -= 1
            papers += counts[hidx]
        
        return hidx
        # citations.sort()
        # for idx in range(len(citations)):
        #     if len(citations) - idx <= citations[idx]:
        #         return len(citations) - idx
        # return 0