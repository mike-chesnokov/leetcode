"""
354. Russian Doll Envelopes

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater
than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
"""
import bisect
from typing import List


class Solution:
    def gready(self, envelopes: List[List[int]]) -> int:
        # wrong answer
        # take next envelope in sorted order or skip it
        # [[1, 1]] -> 1
        # [[1, 1], [2, 2], [2, 7], [4, 3], [4, 10], [5,5]] -> 4
        # [[1, 1], [1, 2], [2, 2]] -> 2
        len_envs = len(envelopes)
        if len_envs == 1:
            return 1

        # sort envelopes by ascending width and ascending height
        sorted_envs = sorted(envelopes, key=lambda x: (x[0], x[1]))
        # print(sorted_envs)
        cnt = 1
        current_env = sorted_envs[0]

        for ind in range(1, len_envs):
            if current_env[0] < sorted_envs[ind][0] \
                    and current_env[1] < sorted_envs[ind][1]:
                cnt += 1
                current_env = sorted_envs[ind]
        return cnt

    def dp(self, envelopes: List[List[int]]) -> int:
        # O(N^2) solution
        len_envs = len(envelopes)
        if len_envs == 1:
            return 1

        dp = [1] * len_envs

        # sort envelopes by ascending width and ascending height
        sorted_envs = sorted(envelopes, key=lambda x: (x[0], x[1]))
        # print(sorted_envs)
        for ind in range(1, len_envs):
            for ind_prev in range(ind - 1, -1, -1):
                if sorted_envs[ind_prev][0] < sorted_envs[ind][0] \
                        and sorted_envs[ind_prev][1] < sorted_envs[ind][1]:
                    # max of current value or previous value + 1
                    dp[ind] = max(dp[ind], dp[ind_prev] + 1)

                # print(sorted_envs[ind_prev], sorted_envs[ind])
                # print('ind_prev=', ind_prev, 'ind=', ind)
                # print('dp=', dp)
                # print('**************')
        return max(dp)

    def bin_search(self, envelopes: List[List[int]]) -> int:
        # O(N Log N) solution
        # after sorting - problem became similar to Longest Increasing Subsequence on heights
        sorted_envs = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        # print(sorted_envs)
        ans = []
        for _, h in sorted_envs:
            # print('h=', h, 'ans=', ans)
            # find the index of current height in answer array
            # using binary search
            ind = bisect.bisect_left(ans, h)
            # print('ind=',ind)
            if ind == len(ans):
                ans.append(h)
            else:
                # if index < len(ans) - replace old value
                # with current height
                ans[ind] = h
                # print('h=', h, 'ans=', ans)
            # print('****************')

        return len(ans)

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # return self.gready(envelopes)  # wrong answer
        # return self.dp(envelopes)  # time limit
        return self.bin_search(envelopes)  # accepted
