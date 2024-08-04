class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ranks = defaultdict(int)
        for road in roads:
            ranks[road[0]] += 1
            ranks[road[1]] += 1
        maxrank = 0
        for i in range(n):
            for j in range(i + 1,  n):
                newrank = ranks[i] + ranks[j]
                if newrank > maxrank:
                    maxrank = newrank - (1 if [i, j] in roads or [j, i] in roads else 0)
        return maxrank