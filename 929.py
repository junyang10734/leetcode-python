# 929. Unique Email Addresses
# String

# https://blog.csdn.net/fuxuemingzhu/article/details/83478570
# runtime: faster than 82.93%
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for e in emails:
            name, domain = e.split('@')
            name = name.split('+')[0].replace('.','')
            res.add(name+'@'+domain)
        return len(res)
