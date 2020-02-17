# Roman to Integer
class Solution1:
    def romanToInt(self, s: str) -> int:
        dic1 = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        dic2 = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        i = 0
        sum = 0
        news = s + '0'
        while i < len(s):
            item = news[i] + news[i+1]
            if item in dic2:
                sum += dic2[item]
                i = i + 2
            else:
                sum += dic1[s[i]]
                i = i + 1

        return sum



class Solution2:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        sum = 0
        for i in range(len(s)):
            if i == 0:
                sum += dic[s[i]]
            else:
                first = dic[s[i-1]]
                second = dic[s[i]]
                if first < second:
                    sum += second - 2*first
                else:
                    sum += second

        return sum


class Solution3:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        n = len(s)
        res = 0
        i = 0
        while i < n:
            if i!=n-1 and d[s[i]] < d[s[i+1]]:
                res += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                res += d[s[i]]
                i += 1
        
        return res
