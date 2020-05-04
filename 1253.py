# Reconstruct a 2-Row Binary Matrix
# Array / Greedy

# runtime: faster than 12.93%
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        res = [[-1]*len(colsum) for i in range(2)]
        ac = 0
        for i,item in enumerate(colsum):
            if item == 0:
                res[0][i] = 0
                res[1][i] = 0
            elif item == 2:
                res[0][i] = 1
                res[1][i] = 1
                ac += 1

        if sum(colsum) == upper + lower and ac <= upper and ac<=lower:
            dif = upper - ac
            for i,item in enumerate(res[0]):
                if item == -1:
                    if dif > 0: 
                        res[0][i] = 1
                        dif -= 1
                    else:
                        res[0][i] = 0

            
            for i,item in enumerate(res[1]):
                if item == -1:
                    if res[0][i] == 1:
                        res[1][i] = 0
                    elif res[0][i] == 0:
                        res[1][i] = 1

        
        for x in range(2):
            for y in range(len(res[0])):
                if res[x][y] == -1:
                    return []
        return res