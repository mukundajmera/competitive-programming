class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.trie
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.end = True

    def search(self, word: str) -> bool:
        def dfs(start, root):
            current = root

            for idx in range(start, len(word)):
                ch = word[idx]
                if ch == ".":
                    #recursive search within children
                    for child in current.children.values():
                        if dfs(idx + 1, child):
                            return True
                    return False
                else:
                    if ch not in current.children:
                        return False
                    current = current.children[ch]
            
            return current.end
        
        return dfs(0, self.trie)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)