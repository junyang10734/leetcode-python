# 299. Bulls and Cows
# hash

# https://blog.csdn.net/fuxuemingzhu/article/details/82872065
# running time: faster than 67.38%
class Solution:
    def getHint(self, secret: str, guess: str) -> str:     
        d = collections.defaultdict(int)
        a, b = 0, 0
        
        for s, g in zip(secret, guess):
            if s == g:
                a += 1
            else:
                d[s] += 1
        
        for i, g in enumerate(guess):
            if secret[i] != guess[i] and d[g]:
                b += 1
                d[g] -= 1
        
        return str(a) + 'A' + str(b) + 'B'
