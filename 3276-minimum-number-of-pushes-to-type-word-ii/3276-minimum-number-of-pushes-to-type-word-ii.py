import string
class Solution:
    def minimumPushes(self, word: str) -> int:
        # Frequency map to store count of each letter
        frequency_map = Counter(word)

        # Priority queue to store frequencies in descending order
        frequency_queue = [-freq for freq in frequency_map.values()]
        heapq.heapify(frequency_queue)

        total_pushes = 0
        index = 0

        # Calculate total number of presses
        while frequency_queue:
            total_pushes += (1 + (index // 8)) * (
                -heapq.heappop(frequency_queue)
            )
            index += 1
        return total_pushes

        # char_map = [0] * 26
        # for ch in word:
        #     char_map[ord(ch) - ord('a')] += 1
        # char_map.sort(reverse=True)
        # # print(char_map)
        # count = 0
        # #total count
        # for idx in range(26):
        #     if char_map[idx] == 0:
        #         continue
        #     count += ((idx // 8) + 1) * char_map[idx]
        #     # print(idx, count)
        # return count