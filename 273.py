# 273. Integer to English Words
# String

# https://leetcode.com/problems/integer-to-english-words/discuss/70632/Recursive-Python
# runtime: faster than 42.08%
class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        
        def word(n):
            if n < 20:
                return to19[n-1:n]
            elif n < 100:
                return [tens[n//10-2]] + word(n%10)
            elif n < 1000:
                return [to19[n//100-1]] + ['Hundred'] + word(n%100)
            else:
                for i,w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                    if n < 1000**(i+1):
                        return word(n//1000**i) + [w] + word(n%1000**i)
        
        return ' '.join(word(num)) or 'Zero'