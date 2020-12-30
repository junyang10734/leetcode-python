# 833. Find And Replace in String
# String
# https://blog.csdn.net/fuxuemingzhu/article/details/81094404

# running time: faster than 47.75% 
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        newS = ''
        i = 0
        while i < len(S):
            if i not in indexes:
                newS += S[i]
                i += 1
            else:
                idx = indexes.index(i)
                source = sources[idx]
                target = targets[idx]
                
                part = S[i:i+len(source)]
                if part == source:
                    newS += target
                else:
                    newS += part
                i += len(source)
        return newS
        