"""
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.climbStairsLoop(n)
        return self.climbStairsRecursive(n)

    @lru_cache(maxsize=None)
    def climbStairsRecursive(self, n: int) -> int:
        if n < 4:
            return n

        return self.climbStairsRecursive(n - 1) + self.climbStairsRecursive(n - 2)

    def climbStairsLoop(self, n: int) -> int:
        # Runtime: 32 ms, faster than 44.53% of Python3 online submissions
        # Memory Usage: 13.7 MB, less than 78.73% of Python3 online submissions
        # num of ways to get to s[i]:
        # s[i] = s[i-1] + s[i-2]
        s_prev = 1
        s_cur = 1

        for ind in range(2, n + 1):
            s_next = s_prev + s_cur
            s_prev = s_cur
            s_cur = s_next

        return s_cur
