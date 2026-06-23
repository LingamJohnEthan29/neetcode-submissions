class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        res = []
        def insertWord(word):
            curr = self.root

            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.endOfWord = True
        
        for word in words:
            insertWord(word)

        ROWS,COLS = len(board), len(board[0])
        res, visit = set(),set()

        def dfs(r,c,node,word):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] not in node.children:
                return 
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                res.add(word)

            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            visit.remove((r,c))


        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j, self.root, "")
            
        return list(res)
