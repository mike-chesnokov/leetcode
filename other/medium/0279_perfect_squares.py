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

    def recursive(self, n: int) -> int:
        if n < 4:
            return n

        # psn_list = [i*i for i in range(1, int(math.sqrt(n)) + 1)]

        self.compute(n, 0)
        return int(self.min_cnt)

    def dp(self, n: int) -> int:
        """Dynamic Programming solution"""
        if n < 4:
            return n

        # get the list or perfect squares to use
        perfect_sqs = [cand * cand
                       for cand in range(1, int(n ** 0.5) + 1)]
        # print(perfect_sqs)

        # process the case then n is square itself
        pss = set(perfect_sqs)
        if n in pss:
            return 1

        dp = list(range(1, n + 1))
        # print(dp)

        for sq in perfect_sqs[1:]:
            for ind in range(1, n):
                residue = (ind + 1) % sq
                if residue == 0:
                    dp[ind] = min(dp[ind],
                                  (ind + 1) // sq)
                    # print(dp[ind],  (ind + 1)// sq)
                else:
                    if ind - sq < 0:
                        dp[ind] = dp[ind]
                    else:
                        dp[ind] = min(dp[ind],
                                      1 + dp[ind - sq])
                        # print(dp[ind],  1 + dp[ind - sq])
                # print('sq =', sq)
                # print('ind =', ind)
                # print('residue =', residue)
                # print(dp[-1])
                # print('****************')

        # print(dp)
        return dp[-1]

    def dp2(self, n: int) -> int:
        """Dynamic Programming optimized solution"""
        dp = list(range(n + 1))

        for ind in range(1, n + 1):
            dp[ind] = min(dp[ind - ind2 * ind2]
                          for ind2 in range(1, int(ind ** 0.5) + 1)) + 1
        return dp[n]

    def bfs(self, n: int) -> int:
        """
        Breadth First Search solution
        """
        if n < 4:
            return n

        # queue of number and cnt of squares
        queue = [(n, 0)]
        seen = set()
        cur_min = n

        while queue:
            # print('************************')
            num, cnt_squares = queue.pop(0)
            # print('num = ', num, 'cnt_squares = ', cnt_squares)

            if num == 0:
                if cnt_squares < cur_min:
                    cur_min = cnt_squares
                    # iterate over perfect squares for current num
            for ind in range(1, int(num ** 0.5) + 1):
                sq = ind * ind
                coef = num // sq
                temp = (num % sq, cnt_squares + coef)
                # print('queue = ', queue)
                # print('temp = ', temp, 'sq = ', sq, 'cur_min = ', cur_min)

                if temp in seen:
                    continue

                if num >= sq and num > 0:
                    queue.append(temp)
                    seen.add(temp)

        return cur_min

    def numSquares(self, n: int) -> int:
        # return self.recursive(n)  # accepted
        # return self.dp(n)  # Time limit exceeded
        return self.dp2(n)  # Accepted solution
        # return self.bfs(n)   # Accepted solution
