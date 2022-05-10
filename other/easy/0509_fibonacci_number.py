"""
509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
"""
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def fib2(self, n: int) -> int:
        """Using python built-in cache decorator"""
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    cache = {}

    def fib(self, n: int) -> int:
        """Using manual cache"""
        if n in self.cache:
            return self.cache[n]
        if n < 2:
            return n
        res = self.fib(n - 1) + self.fib(n - 2)

        self.cache[n] = res

        return res
