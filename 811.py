# 811. Subdomain Visit Count
# Hash Table

# runtime: O(n)
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for domain in cpdomains:
            l = domain.split()
            count = int(l[0])
            l = l[1].split('.')
            for i in range(len(l)):
                item = '.'.join(l[i:])
                if item in d:
                    d[item] += count
                else:
                    d[item] = count
        
        res = []
        for key,value in d.items():
            res.append(str(value) + ' ' + key)
        return res