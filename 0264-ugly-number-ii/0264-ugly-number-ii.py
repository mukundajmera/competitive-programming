import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = [1]
        seen = set()
        factors = [2,3,5]

        current = 1
        for _ in range(n):
            current = heapq.heappop(min_heap)
            for factor in factors:
                if(next_num:= current*factor) not in seen:
                    heapq.heappush(min_heap, next_num)
                    seen.add(next_num)
        return current 

        # ugly = set([1])
        # current = 1

        # for idx in range(n):
        #     current = min(ugly)
        #     ugly.remove(current)

        #     ugly.add(current*2)
        #     ugly.add(current*3)
        #     ugly.add(current*5)
        # return current

        