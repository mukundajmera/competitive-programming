class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct_words = OrderedDict()
        for word in arr:
            if word in distinct_words:
                distinct_words[word] += 1
            else:
                distinct_words[word] = 1
        word = ""
        for key, value in distinct_words.items():
            if value > 1:
                continue
            elif value == 1:
                k -= 1
                if k == 0:
                    word = key
                    break
        return word                    