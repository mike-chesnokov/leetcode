"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""


class Solution:
    match = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    def stack(self, s: str) -> bool:
        """
        Use stack for open brackets
        """
        closed_brackets = set([')', '}', ']'])
        stack_open = []

        for bracket in s:
            # print('bracket = ', bracket)
            # print('stack_open = ', stack_open)
            if len(stack_open) > 0:
                if bracket in closed_brackets:
                    last_open = stack_open.pop()
                    if bracket != self.match[last_open]:
                        return False
                else:
                    stack_open.append(bracket)
            else:
                if bracket in closed_brackets:
                    return False
                stack_open.append(bracket)

        if len(stack_open) == 0:
            return True
        else:
            return False

    def replace(self, s: str) -> bool:
        """
        Replacing paired brackets
        """
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')

        if len(s) == 0:
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        # return self.stack(s)
        return self.replace(s)
