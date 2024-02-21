# 793. Preimage Size of Factorial Zeroes Function
# Math / Binary Search

# https://algo.monster/liteproblems/793
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # Recursive function to count trailing zeroes in factorial of x
        def count_trailing_zeroes(x):
            # Base case: when x is 0, it contributes no trailing zeroes
            if x == 0:
                return 0
            # Recursive case: x contributes x // 5 trailing zeroes
            # plus count of trailing zeroes from all multiples of 5 less than x
            return x // 5 + count_trailing_zeroes(x // 5)

        # Function to find the left boundary of K's preimage using binary search
        # It finds the smallest number whose factorial has exactly k trailing zeroes
        def left_boundary_of_k(k):
            # Perform a binary search on the range [0, 5*k)
            # Since any number have at most k trailing zeroes in its factorial
            return bisect.bisect_left(range(5 * k), k, key=count_trailing_zeroes)

        # The size of the preimage for any valid k is always 5
        # This is because factorial(n) for values of n between two consecutive
        # multiples of 5 have the same number of trailing zeroes
        # We can use this by checking the difference between the left boundaries
        # of k and k+1. If there's a valid preimage size, it will always be 5.
        # If it is zero, then there is no number whose factorial ends with k zeroes.
        return left_boundary_of_k(k + 1) - left_boundary_of_k(k)