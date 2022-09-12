"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive,
 return all possible letter combinations that the number could represent.
 Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].
"""
from typing import List


class Solution:
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def __init__(self):
        self.result = []

    def backtrack(self, digits: str, cur_ind: int, cur_str: str) -> None:
        """
        Iterate over digits using cur_ind,
        save current str to cur_str
        """
        if digits == '':
            return

        # base case
        if len(cur_str) == len(digits):
            self.result.append(cur_str)
            return
            # process candidates
        for letter in self.mapping[digits[cur_ind]]:
            # go to next digit
            self.backtrack(digits, cur_ind + 1, cur_str + letter)

    def letterCombinations(self, digits: str) -> List[str]:
        self.backtrack(digits, 0, '')
        return self.result
