class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels_sum = [0] * (len(words) + 1)
        vowel = "aeiou"
        current_val = 0
        for idx, word in enumerate(words):
            if word[0] in vowel and word[-1] in vowel:
                current_val += 1
            vowels_sum[idx+1] = current_val
        
        answer = []
        for query in queries:
            start, end = query[0], query[1]
            answer.append(vowels_sum[end+1] - vowels_sum[start])
        return answer