# Sort Characters By Frequency
# Hash Table


# runtime: faster than 70.72% 
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict(lambda:0)
        for k in s:
            counter[k] += 1
        
        d = sorted(counter.items(), key=lambda item:item[1], reverse=True)

        res = ''
        for item in d:
            res += item[1] * item[0]
    
        return res
