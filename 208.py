# Implement Trie (Prefix Tree)
# Design

# https://blog.csdn.net/fuxuemingzhu/article/details/79388432
# https://leetcode.com/articles/implement-trie-prefix-tree/
# Tree
# runtime: faster than 43.23%

class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False
    

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current == None:
                return False
        return current.isword
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True
        


# https://maxming0.github.io/2020/05/14/Implement-Trie-Prefix-Tree/
# Hash / Recursive
# running time: faster than 99.66% 
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.d
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.d
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        return '#' in cur
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.d
        for w in prefix:
            if w not in cur:
                return False
            cur = cur[w]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)