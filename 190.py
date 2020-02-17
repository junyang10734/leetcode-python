# Reverse Bits

# bin(n): convert an decimal to binary
# int(b,2): convert an binary to int
# faster than 94.82%
class Solution1:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[2:][::-1]
        b = b + '0' * (32 - len(b))
        return int(b, 2)    


# naive method
# We only need to reversed n from right to left by one bit. 
# If the number be taken out is 1, move the result res left by one bit and add 1
# If 0 is taken out, move the result res to the left by one bit
# Then move n to the right by one bit
# faster than 82.68%
class Solution2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            if n & 1 == 1:
                res = (res << 1) + 1
            else:
                res = res << 1
            n = n >> 1
            
        return res


# simplify solution2
class Solution3:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = res << 1
            if n & 1 == 1:
                res += 1
            n = n >> 1
            
        return res


# simplify solution3
# faster than 99.04%
class Solution4:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n = n >> 1
            
        return res