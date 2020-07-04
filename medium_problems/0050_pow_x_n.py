"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100

Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:

    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Runtime: 36 ms, faster than 24.43% of Python3 online submissions
        # Memory Usage: 13.9 MB, less than 36.98% of Python3 online submissions
        # n in binary view is sum of powers of 2
        # n = 13 = 1101
        # only last bit = n % 2
        # drop last bit : n = n // 2
        
        if n < 0:
            is_less_zero = True
            n *= -1
        else:
            is_less_zero = False
        
        res = 1
        mult = x
        
        while n != 0:
            if n % 2 != 0:
                res *= mult
            mult *= mult
            n = n // 2
        
        if is_less_zero:
            res = 1 / res
        
        return res
