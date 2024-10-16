class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        queue = []
        if a:
            heapq.heappush(queue, (-a, "a"))
        if b:
            heapq.heappush(queue, (-b, "b"))
        if c:
            heapq.heappush(queue, (-c, "c"))
        
        result = []
        # print(queue)
        while queue:
            count, ch = heapq.heappop(queue)
            count = -count
            if(len(result) >= 2 and result[-1] == ch and result[-2] == ch):
                if not queue:
                    break
                tempCount, tempChar = heapq.heappop(queue)
                result.append(tempChar)
                if (tempCount + 1) < 0:
                    heapq.heappush(queue, (tempCount + 1, tempChar))
                heapq.heappush(queue, (-count, ch))
            else:
                count -= 1
                result.append(ch)
                if count > 0:
                    heapq.heappush(queue, (-count, ch))
        
        return "".join(result)

    