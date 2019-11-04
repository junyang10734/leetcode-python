# Group Anagrams

# runtime： O(nk) faster than 84.76%
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for x in strs:
            s = list(x)
            s.sort()
            s = ''.join(s)
            if s in dic:
                l = dic[s]
                l.append(x)
                dic[s] = l
            else:
                l = [x]
                dic[s] = l
        res = []
        for key in dic:
            res.append(dic[key])
        return res