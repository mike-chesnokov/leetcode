"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
    1 <= n <= 8
"""
from typing import List


class Solution:

    def __init__(self):
        self.result = []

    def is_valid(self, string) -> bool:
        """
        Check if string a valid combination of Parentheses
        """
        while '()' in string or '{}' in string or '[]' in string:
            string = string.replace('()', '').replace('[]', '').replace('{}', '')

        return len(string) == 0

    def recursion(self, cnt_opened: int, cnt_closed: int, cur_str: str) -> None:
        """
        Recursive approach
        """
        if cnt_opened == 0 and cnt_closed == 0 and self.is_valid(cur_str):
            self.result.append(cur_str)
            return

        if cnt_opened > 0:
            self.recursion(cnt_opened - 1, cnt_closed, cur_str + '(')

        if cnt_closed > 0:
            self.recursion(cnt_opened, cnt_closed - 1, cur_str + ')')

    def recursion2(self, cnt_opened: int, cnt_closed: int, cur_str: str) -> None:
        """
        Optimized Recursive approach without validation of string
        """
        if cnt_opened == 0 and cnt_closed == 0:
            self.result.append(cur_str)
            return

        if cnt_opened > 0:
            self.recursion(cnt_opened - 1, cnt_closed, cur_str + '(')

        if cnt_closed > cnt_opened:
            self.recursion(cnt_opened, cnt_closed - 1, cur_str + ')')

    def iteration(self, n: int) -> List[str]:
        """
        Iterative approach
        """
        result = []
        stack = ['(']

        while stack:

            cur_string = stack.pop()

            if len(cur_string) == 2 * n and self.is_valid(cur_string):
                result.append(cur_string)

            if len(cur_string) < 2 * n:
                for candidate in ['(', ')']:
                    stack.append(cur_string + candidate)

        return result

    def generateParenthesis(self, n: int) -> List[str]:
        # self.recursion(n, n, "")  # Accepted
        # self.recursion2(n, n, "")  # Accepted
        # return self.result
        return self.iteration(n)  # Accepted
