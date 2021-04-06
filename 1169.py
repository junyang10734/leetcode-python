# 1169. Invalid Transactions
# Array / String

# runtime: faster than 23.15%
class Solution1:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        d = collections.defaultdict(list)
        for t in transactions:
            arr = t.split(',')
            d[arr[0]].append(arr)
        
        for k in d:
            arr = d[k]
            if len(arr) == 1 and int(arr[0][2]) > 1000:
                res.append(','.join(arr[0]))
                
            seen = set()   
            for i in range(len(arr)-1):
                if int(arr[i][2]) > 1000:
                    if i not in seen:
                            res.append(','.join(arr[i]))
                            seen.add(i)
                            
                for j in range(i+1, len(arr)):  
                    if int(arr[j][2]) > 1000:
                        if j not in seen:
                            res.append(','.join(arr[j]))
                            seen.add(j)
                            
                    if(abs(int(arr[i][1]) - int(arr[j][1]))) <= 60 and arr[i][3] != arr[j][3]:
                        if i not in seen:
                            res.append(','.join(arr[i]))
                            seen.add(i)
                        if j not in seen:
                            res.append(','.join(arr[j]))
                            seen.add(j)
        return res


# Sort
# https://leetcode.com/problems/invalid-transactions/discuss/366332/python-sort-solution
# runtime: faster than 67.22%
class Solution2:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        t = [x.split(',') for x in transactions]
        t.sort(key=lambda x:(x[0], int(x[1])))
        i = 0
        seen = set()
        
        while i < len(t):
            j = i + 1
            duplicate = False
            while j < len(t) and t[j][0] == t[i][0] and int(t[j][1]) - int(t[i][1]) <= 60:
                if t[j][3] != t[i][3]:
                    duplicate = True
                j += 1
            
            if duplicate:
                k = i
                while k < j:
                    seen.add(k)
                    k += 1
            elif int(t[i][2]) > 1000:
                seen.add(i)
            i += 1
        
        return [','.join(t[i]) for i in seen]