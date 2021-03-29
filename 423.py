# 423. Reconstruct Original Digits from English
# Math

# https://leetcode.com/problems/reconstruct-original-digits-from-english/solution/
# runtime: faster than 86.9%
class Solution:
    def originalDigits(self, s: str) -> str:
        count = collections.Counter(s)
        res = {}
        res['0'] = count['z']
        res['2'] = count['w']
        res['4'] = count['u']
        res['6'] = count['x']
        res['8'] = count['g']
        res['3'] = count['h'] - res['8']
        res['5'] = count['f'] - res['4']
        res['7'] = count['s'] - res['6']
        res['9'] = count['i'] - res['5'] - res['6'] - res['8']
        res['1'] = count['n'] - res['7'] - 2*res['9']
        output = [key * res[key] for key in sorted(res.keys())]
        return ''.join(output)