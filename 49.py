# Group Anagrams

# runtime： O(nk) faster than 84.76%
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            l = list(s)
            l.sort()
            d[''.join(l)].append(s)
        
        res = []
        for k,v in d.items():
            res.append(v)
        return res