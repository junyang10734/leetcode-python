# Search Suggestions System
# String

# runtime: faster than 23.01%
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        for i in range(len(searchWord)):
            res = []
            s = searchWord[:i+1]
            for item in products:
                if len(res) >= 3:
                    break
                if item[:i+1] == s:
                    res.append(item)
            ans.append(res)                    
        return ans  