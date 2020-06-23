# Word Ladder
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/82903681

# BFS
# runtime: faster than 46.40%
class Solution1:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        
        visited = set([beginWord])
        chrs = [chr(ord('a') + i) for i in range(26)]
        bfs = collections.deque([beginWord])
        res = 1
        
        while bfs:
            len_bfs = len(bfs)
            for _ in range(len(bfs)):
                origin = bfs.popleft()
                for i in range(len(origin)):
                    originlist = list(origin)
                    for c in chrs:
                        originlist[i] = c
                        transword = ''.join(originlist)
                        if transword not in visited:
                            if transword == endWord:
                                return res + 1
                            elif transword in wordset:
                                bfs.append(transword)
                                visited.add(transword)
            res += 1
        
        return 0


# BFS
# runtime: faster than 36.77% 
class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        bfs = collections.deque()
        bfs.append((beginWord, 1))
        
        while bfs:
            word, length = bfs.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordset and newWord != word:
                        wordset.remove(newWord)
                        bfs.append((newWord, length + 1))
        return 0
