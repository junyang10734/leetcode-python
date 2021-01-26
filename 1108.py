# 1108. Defanging an IP Address
# String


# runtime: faster than 5.81%
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
