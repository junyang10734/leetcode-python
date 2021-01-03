# 792. Number of Matching Subsequences

# https://blog.csdn.net/fuxuemingzhu/article/details/82834760

# faster than 41.97%
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        d = collections.defaultdict(list)
        for i, s in enumerate(S):
            d[s].append(i)

        res = 0
        m = {}
        for word in words:
            if word in m:
                res += 1
            else:
                prev = -1
                count = 0
                for w in word:
                    i = bisect.bisect_left(d[w], prev + 1)
                    if i < len(d[w]):
                        prev = d[w][i]
                        count += 1
                        if(count == len(word)):
                            res += 1
                            count = 0
                            m[word] = 1
        return res


# faster than 50.73%
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        d = collections.defaultdict(list)
        for i,s in enumerate(S):
            d[s].append(i)
        
        m = {}
        def isMatch(word, d):
            if word in m:
                return 1
            prev = -1
            for w in word:
                i = bisect.bisect_left(d[w], prev+1)
                if i == len(d[w]):
                    return 0
                prev = d[w][i]
            m[word] = 1
            return 1
        
        res = [isMatch(word,d) for word in words]
            
        return sum(res)
                    