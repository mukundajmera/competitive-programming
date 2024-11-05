class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        length = len(words)
        last = words[length-1][-1]

        for idx in range(length):
            if words[idx][0] != last:
                return False
            last = words[idx][-1]
        
        return True