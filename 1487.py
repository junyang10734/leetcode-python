# 1487. Making File Names Unique
# String / Hash Table

# runtime: faster than 74.49%
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d = {}
        res = []
        for name in names:
            count = d.get(name, 0)
            prev_name = name
            if count > 0:
                while prev_name in d:
                    prev_name = name + '(' + str(count) + ')'
                    count += 1
                d[name] = count
            d[prev_name] = 1
            res.append(prev_name)
        return res