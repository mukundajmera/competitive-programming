class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])
        result, visited = set(), set()

        def dfs(r, c, node, word):
            if (
                r not in range(rows)
                or c not in range(cols)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visited
            ):
                return
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            
            #when found the word check if exist
            if node.isWord:
                node.isWord = False
                result.add(word)
                root.removeWord(word)
            
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c, root, "")
        
        return list(result)