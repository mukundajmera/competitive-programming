class Solution:            
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        char_map = {}
        for word in strs:
            # value = sorted(word)
            value = "".join(sorted(word))
            # print(word, value)
            if value in char_map:
                char_map[value].append(word)
            else:
                char_map[value] = [word]
        for value in char_map.values():
            groups.append(value)
        return groups