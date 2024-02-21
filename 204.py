# Count Primes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        else:
            isPrime = [True] * n
            for i in range(2,int(n**0.5)+1):
                if isPrime[i] == False:
                    continue
                else:
                    j = i*i
                    while j < n:
                        isPrime[j] = False
                        j = j + i
        
            return isPrime.count(True)-2


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
            
        isPrime = [True] * n
        for i in range(2, int(n**0.5)+1):
            if isPrime[i]:
                for j in range(i**2, n, i):
                    isPrime[j] = False
        
        return isPrime.count(True)-2
        