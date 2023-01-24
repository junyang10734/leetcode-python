# 93. Restore IP Addresses
# backtrack

# https://leetcode.com/problems/restore-ip-addresses/solutions/31140/python-easy-to-understand-solution-backtracking/?orderBy=most_votes
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(s, idx, path):
            if idx > 4:
                return
            if idx == 4 and not s:
                res.append(path[:-1])
                return

            for i in range(1, len(s)+1):
                if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                    backtrack(s[i:], idx+1, path + s[:i] + '.')
                
        
        backtrack(s, 0, "")
        return res
