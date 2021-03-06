# Find the Town Judge
# Graph / Hash Table

# hash
# runtime: faster than 23.31%
class Solution1:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            return 1
        trust_dic = {}
        be_trust_dic = {}

        for i in trust:
            if i[0] not in trust_dic:
                trust_dic[i[0]] = []
            trust_dic[i[0]].append(i[1])
            
            if i[1] not in be_trust_dic:
                be_trust_dic[i[1]] = []
            be_trust_dic[i[1]].append(i[0])
        
        if len(trust_dic) != N-1:
            return -1
        
        for i in range(1,N+1):
            if i not in trust_dic:
                if len(be_trust_dic[i]) == N-1:
                    return i
        
        return -1


# graph 
# in/out degree
# runtime: faster than 87.04%
class Solution2:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        res = -1
        d = [0]*(N+1)
        for item in trust:
            d[item[1]] += 1
            d[item[0]] -= 1
            
        for i in range(N+1):
            if d[i] == N-1:
                res = i 
        return res