# 1056. Confusing Number
# Hash Table

class Solution:
    def confusingNumber(self, n: int) -> bool:
        mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        res = ''
        for i in str(n):
            if i not in mapping:
                return False
            res = mapping[i] + res

        return int(res) != n