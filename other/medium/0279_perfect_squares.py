"""
279. Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer;
in other words, it is the product of some integer with itself.
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

import math


class Solution:
    min_cnt = float("inf")

    def compute(self, n: int, cum_cnt: int):
        if n == 0:
            self.min_cnt = min(self.min_cnt, cum_cnt)

        sqrt_ = int(math.sqrt(n))
        for ind in range(sqrt_, 0, -1):
            coef = n // (ind * ind)
            diff = n - (ind * ind) * coef
            # print(diff, coef, (ind*ind), self.min_cnt, cum_cnt)
            if cum_cnt + coef < self.min_cnt:
                self.compute(diff, cum_cnt + coef)

        # solution with timeout
        # for psn in psn_list:
        #    coef = n // psn
        #    diff = n - psn * coef
        #    if cum_cnt + coef < self.min_cnt:
        #        self.compute(diff, psn_list[1:].copy(), cum_cnt + coef)

    def numSquares(self, n: int) -> int:
        if n < 4:
            return n

        # psn_list = [i*i for i in range(1, int(math.sqrt(n)) + 1)]

        self.compute(n, 0)
        return int(self.min_cnt)
