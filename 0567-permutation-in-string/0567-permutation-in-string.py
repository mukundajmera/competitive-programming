class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        
        if n1 > n2: return False

        s1Count = [0] * 26
        s2Count = [0] * 26
        
        # initial values for first set of window
        for i in range(n1):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        for i in range(n2-n1):               # n2-n1 is the number of slides
            if s1Count == s2Count:
                return True
            
            # reduce leaving char count
            s2Count[ord(s2[i]) - ord('a')] -= 1
            
            # increase introduced char count
            s2Count[ord(s2[i+n1]) - ord('a')] += 1

        return s1Count == s2Count  
        # cntr, w, match = Counter(s1), len(s1), 0     

        # for i in range(len(s2)):
        #     if s2[i] in cntr:
        #         if not cntr[s2[i]]:
        #             match -= 1
        #         cntr[s2[i]] -= 1
        #         if not cntr[s2[i]]:
        #             match += 1

        #     if i >= w and s2[i-w] in cntr:
        #         if not cntr[s2[i-w]]:
        #             match -= 1
        #         cntr[s2[i-w]] += 1
        #         if not cntr[s2[i-w]]:
        #             match += 1

        #     if match == len(cntr):
        #         return True

        # return False