# 734. Sentence Similarity

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        d = collections.defaultdict(set)
        for x, y in similarPairs:
            d[x].add(y)
            d[y].add(x)
        
        for x, y in zip(sentence1, sentence2):
            if x == y:
                continue
            elif y in d[x] and x in d[y]:
                continue
            else:
                return False
        
        return True
