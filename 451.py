# Sort Characters By Frequency
# Hash Table

# defaultdict
# runtime: faster than 70.72% 
class Solution1:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict(lambda:0)
        for k in s:
            counter[k] += 1
        
        d = sorted(counter.items(), key=lambda item:item[1], reverse=True)

        res = ''
        for item in d:
            res += item[1] * item[0]
    
        return res


# Counter
# runtime: faster than 99.00%
class Solution2:
    def frequencySort(self, s: str) -> str:
        d = collections.Counter(s).most_common()
        res = ''
        for i in enumerate(d):
            res += i[1][0]*i[1][1]
        return res