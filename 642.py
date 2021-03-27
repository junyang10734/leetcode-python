# 642. Design Search Autocomplete System
# Design / Trie

# http://bookshadow.com/weblog/2017/07/16/leetcode-design-search-autocomplete-system/
# runtime: faster than 88.01%
class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = set()

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.buffer = ''
        self.stimes = collections.defaultdict(int)
        self.trie = TrieNode()
        for s,t in zip(sentences, times):
            self.stimes[s] = t
            self.addSentence(s)
        self.tnode = self.trie
            
    def input(self, c: str) -> List[str]:
        res = []
        if c != '#':
            self.buffer += c
            if self.tnode:
                self.tnode = self.tnode.children.get(c)
            if self.tnode:
                res = sorted(self.tnode.sentences, key=lambda x:(-self.stimes[x], x))[:3]
        else:
            self.stimes[self.buffer] += 1
            self.addSentence(self.buffer)
            self.buffer = ''
            self.tnode = self.trie
        return res
    
    def addSentence(self, sentence):
        node = self.trie
        for letter in sentence:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
            child.sentences.add(sentence)
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)