"""
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string],
where the encoded_string inside the square brackets is being repeated exactly k times.
 Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid;
there are no extra white spaces, square brackets are well-formed, etc.
 Furthermore, you may assume that the original data does not contain any digits and
 that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:
    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].
"""


class Solution:

    def iterative(self, s: str) -> str:
        """
        Iterative using stack with digits and letters
        """
        stack = []  # to store tuples of (digit, cur_string)
        cur_letters = ''
        cur_digit = ''
        result = ''

        for symbol in s:
            # print('*********************')
            # print('symbol = ', symbol)
            # print('stack = ', stack)
            # print('cur_letters = ', cur_letters)
            # print('cur_digit = ', cur_digit)

            if symbol.isdigit():
                cur_digit += symbol

            if symbol.isalpha():
                cur_letters += symbol

            if symbol == '[':
                # process digit and letters
                stack.append((int(cur_digit), cur_letters))
                cur_digit = ''
                cur_letters = ''

            if symbol == ']':
                prev_digit, prev_letters = stack.pop()
                # accumulate previous letters and multiply cur string
                cur_letters = prev_letters + cur_letters * prev_digit

            # print('AFTER')
            # print('stack = ', stack)
            # print('cur_letters = ', cur_letters)
            # print('cur_digit = ', cur_digit)

        return cur_letters

    def decodeString(self, s: str) -> str:
        return self.iterative(s)
