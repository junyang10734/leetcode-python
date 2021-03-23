# 966. Vowel Spellchecker
# Hash Table

# https://blog.csdn.net/fuxuemingzhu/article/details/85389781
# runtime: faster than 71.84%
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordset = set(wordlist)
        capdict = {word.lower(): word for word in wordlist[::-1]}
        vodict = {re.sub(r'[aeiou]', '#', word.lower()): word for word in wordlist[::-1]}
        
        res = []
        for q in queries:
            if q in wordset:
                res.append(q)
            elif q.lower() in capdict:
                res.append(capdict[q.lower()])
            elif re.sub(r'[aeiou]', '#', q.lower()) in vodict:
                res.append(vodict[re.sub(r'[aeiou]', '#', q.lower())])
            else:
                res.append('')
        return res