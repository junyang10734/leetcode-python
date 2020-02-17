# Count and Say
class Solution1:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(n-1):
            new_res, pre, count = '', res[0], 0
            for j in range(len(res)):
                if res[j] == pre:
                    count += 1
                else:
                    new_res += str(count) + pre
                    count = 1
                    pre = res[j]
            res = new_res + str(count) + pre
        return res


# Use recursions, easier to understand
# faster than solution1
class Solution2:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        s = self.countAndSay(n-1)
        res = ''
        count = 0
        for i in range(len(s)):
            count += 1
            if i == len(s) -1 or s[i] != s[i+1]:
                res += str(count) + s[i]
                count = 0
        
        return res