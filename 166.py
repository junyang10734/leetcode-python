# Fraction to Recurring Decimal

# https://www.youtube.com/watch?v=zy8sJ_Wx7y8
# run time: faster than 94.06%
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, d = numerator, denominator
        negative_flag = '-' if n*d < 0 else ''
        n, d = abs(n), abs(d)
        
        numlist = []
        cnt = 0
        loopDic = {}
        loopStr = None
        
        while True:
            numlist.append(str(n // d))
            cnt += 1
            n = 10 * (n % d)
            if n == 0:
                break
                
            if n in loopDic:
                loc = loopDic[n]
                loopStr = ''.join(numlist[loc: cnt])
                break
            else:
                loopDic[n] = cnt
        
        ans = negative_flag + numlist[0]
        if len(numlist) > 1:
            ans += '.'
            
        if loopStr:
            ans += ''.join(numlist[1:len(numlist)-len(loopStr)]) + '(' + loopStr + ')'
        else:
            ans += ''.join(numlist[1:])
        
        return ans