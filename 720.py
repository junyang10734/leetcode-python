# 720. Longest Word in Dictionary

# Array / set
# https://blog.csdn.net/fuxuemingzhu/article/details/79123277
# running time: faster than 83.80% 
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        dic = set([''])
        longestWord = ''

        for word in words:
            if word[:-1] in dic:
                dic.add(word)
                if len(word) > len(longestWord):
                    longestWord = word

        return longestWord