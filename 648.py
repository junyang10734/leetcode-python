# 648. Replace Words
# Hash Table / Trie
# compare 208

# Hash
# runtime: faster than 38.38%
class Solution1:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = set(dictionary)
        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in d:
                    return word[:i]
            return word
        
        return ' '.join([replace(word) for word in sentence.split(' ')])


# Trie
# runtime: faster than 98.79%
class Trie:
    def __init__(self):
        self.d = {}
        
    def insert(self, word: str) -> None:
        cur = self.d
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['#'] = True

    def search(self, word: str) -> bool:
        cur = self.d
        ans = ''
        for w in word:
            if w not in cur:
                return ''
            ans += w
            cur = cur[w]
            if '#' in cur:
                return ans
        return ans if '#' in cur else ''
        

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        res = []
        for word in sentence.split():
            t = trie.search(word)
            res.append(word if t == '' else t)
        return ' '.join(res)