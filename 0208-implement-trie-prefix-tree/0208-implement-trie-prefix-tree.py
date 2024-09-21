class Trie:

    def __init__(self):
        self.trie = {"*" : ""}

    def insert(self, word: str) -> None:
        current = self.trie
        for ch in word:
            if not ch in current:
                current[ch] = {}
            current = current[ch]
        print(current)
        current["*"] = {} 

    def search(self, word: str) -> bool:
        found = True
        current = self.trie
        # print(current)
        for ch in word:
            if not ch in current:
                return False
            else:
                current = current[ch]
        if current.get("*") is None:
            found = False
        return found

    def startsWith(self, prefix: str) -> bool:
        found = True
        current = self.trie
        for ch in prefix:
            if ch not in current:
                return False
            current = current[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)