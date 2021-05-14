# 957. Prison Cells After N Days
# Hash Table

# https://leetcode.com/problems/prison-cells-after-n-days/solution/
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        d = {}
        isforwarded = False
        
        while n > 0:
            if not isforwarded:
                state_key = tuple(cells)
                if state_key in d:
                    n %= d[state_key] - n
                    isforwarded = True
                else:
                    d[state_key] = n
            
            if n > 0:
                n -= 1
                next_cells = self.nextDay(cells)
                cells = next_cells
                
        return cells
    
    def nextDay(self, cells):
        ret = [0]
        for i in range(1, len(cells)-1):
            ret.append(int(cells[i-1] == cells[i+1]))
        ret.append(0)
        return ret
