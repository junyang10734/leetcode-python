# 244. Shortest Word Distance II
# Design / Hash Table

# runtime: faster than 88.18%
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = collections.defaultdict(list)
        for i,word in enumerate(wordsDict):
            self.d[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.d[word1], self.d[word2]
        res = float('inf')
        n1, n2 = 0, 0
        while n1 < len(l1) and n2 < len(l2):
            res = min(res, abs(l1[n1]-l2[n2]))
            if l1[n1] < l2[n2]:
                n1 += 1
            else:
                n2 += 1
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)