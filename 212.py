# 212. Word Search II
# Backtrack / Trie

# https://leetcode.com/problems/word-search-ii/solution/
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_key = '#'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[word_key] = word
        
        m, n = len(board), len(board[0])
        matchedWords = []
        
        def backtrack(i, j, parent):
            letter = board[i][j]
            currNode = parent[letter]
            
            word_match = currNode.pop(word_key, False)
            if word_match:
                matchedWords.append(word_match)
            board[i][j] = ''
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx, ny = i+dx, j+dy
                if 0<=nx<m and 0<=ny<n and board[nx][ny] in currNode:
                    backtrack(nx, ny, currNode)
            board[i][j] = letter
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtrack(i, j, trie)
                    
        return matchedWords
        