# 482. License Key Formatting
# string

# running time: faster than 95.76%
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-','').upper()

        f = len(S) % K
        n = len(S) // K
        
        if f == 0:
            res = ''
        else:
            res = S[:f]
            res += '-'
        
        S = S[f:]
        
        for i in range(n):
            res += S[K*i: K*(i+1)] + '-'
        
        return res[:-1]
        