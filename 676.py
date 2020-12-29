# 676. Implement Magic Dictionary

# hash table
# https://leetcode.com/problems/implement-magic-dictionary/solution/

# running time: faster than 70.55% 
class MagicDictionary1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = collections.defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.buckets[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        return any(sum(a!=b for a,b in zip(searchWord, word)) == 1 for word in self.buckets[len(searchWord)])


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)



# running time: faster than 54.74% 
class MagicDictionary2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
    
    def _genneighbors(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i+1:]

    def buildDict(self, dictionary: List[str]) -> None:
        self.dictionary = set(dictionary)
        self.count = collections.Counter(nei for word in dictionary for nei in self._genneighbors(word))

    def search(self, searchWord: str) -> bool:
        return any(self.count[nei] > 1 or self.count[nei] == 1 and searchWord not in self.dictionary for nei in self._genneighbors(searchWord))


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)