# Divide Two Integers

# https://leetcode.com/problems/divide-two-integers/discuss/427345/Python-24ms-beats-99-with-and-wo-bitwise-operators

# bitwise operators
# run time: faster than 99.14%
class Solution1:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum << 1) <= dividend:
                the_sum <<= 1
                current_quotient <<= 1            
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))


# without bitwise operators
# run time: faster than 96.67%
class Solution2:
    def divide(self, dividend: int, divisor: int) -> int:
	    is_negative = (dividend < 0) != (divisor < 0)
	    divisor, dividend = abs(divisor), abs(dividend)

	    quotient = 0
	    the_sum = divisor

	    while the_sum <= dividend:
		    current_quotient = 1
		    while (the_sum + the_sum) <= dividend:
			    the_sum += the_sum
			    current_quotient += current_quotient
		    dividend -= the_sum
		    the_sum = divisor
		    quotient += current_quotient

	    return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))