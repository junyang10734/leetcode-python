# Search Suggestions System
# String

# runtime: faster than 23.01%
class Solution1:
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


# https://blog.csdn.net/Orientliu96/article/details/104101844
# runtime: faster than 72.34%
class Solution2:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        for i in range(1, len(searchWord)+1):
            products = list(filter(lambda x:x.startswith(searchWord[:i]), products))
            res.append(products[:3])
        return res