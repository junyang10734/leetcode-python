# 989. Add to Array-Form of Integer
# Array / Math

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)-1, -1, -1):
            k, num[i] = divmod(k + num[i], 10)
        
        return [int(i) for i in str(k)] + num if k else num


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return [int(i) for i in list(str(int(''.join([str(n) for n in num])) + k))]