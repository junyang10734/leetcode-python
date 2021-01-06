# 777. Swap Adjacent in LR String

# String / Two Pointers
# https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/997747/Python-One-pass-O(n)-time-O(1)-space-faster-than-98.83
# running time: faster than 100.00%
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_surplus_R = 0
        end_surplus_L = 0
        
        for c1,c2 in zip(start, end):
            if c1 == c2:
                if c1 == 'X':
                    continue
                elif c1 == 'R' and end_surplus_L == 0:
                    continue
                elif c1 == 'L' and start_surplus_R == 0:
                    continue
                else:
                    return False
        
            if c1 == 'X' and c2 == 'L' and start_surplus_R == 0:
                end_surplus_L += 1
            elif c1 == 'L' and c2 == 'X' and start_surplus_R == 0 and end_surplus_L > 0:
                end_surplus_L -= 1
            elif c1 == 'R' and c2 == 'X' and end_surplus_L == 0:
                start_surplus_R += 1
            elif c1 == 'X' and c2 == 'R' and end_surplus_L == 0 and start_surplus_R > 0:
                start_surplus_R -= 1
            else:
                return False
        
        return start_surplus_R == 0 and end_surplus_L == 0
