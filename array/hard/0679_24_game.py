"""
679. 24 Game

You are given an integer array cards of length 4.
You have four cards, each containing a number in the range [1, 9].
You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/']
and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

    The division operator '/' represents real division, not integer division.
        For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
    Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
        For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
    You cannot concatenate numbers together
        For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
Return true if you can get such expression that evaluates to 24, and false otherwise.

Example 1:
Input: cards = [4,1,8,7]
Output: true
Explanation: (8-4) * (7-1) = 24

Example 2:
Input: cards = [1,2,1,2]
Output: false
"""
from typing import List
from itertools import permutations


class Solution:

    def generate_variants(self, num1: int, num2: int) -> List[float]:
        variants = [num1 + num2, num1 - num2, num2 - num1, num1 * num2]
        if num1:
            variants.append(num2 / num1)
        if num2:
            variants.append(num1 / num2)
        return variants

    def backtracking(self, cards: List[int]) -> bool:
        # base case
        if len(cards) == 1:
            return abs(cards[0] - 24.0) <= 0.01

        # iterate over pairs of numbers
        for ind1 in range(len(cards)):
            for ind2 in range(ind1 + 1, len(cards)):
                new_cards = [el for ind, el in enumerate(cards)
                             if ind != ind1 and ind != ind2]
                # iterate over every possible operation over pair
                for cur_num in self.generate_variants(num1=cards[ind1],
                                                      num2=cards[ind2]):
                    new_cards.append(cur_num)
                    # try new array
                    if self.backtracking(new_cards):
                        return True
                    # if False - drop number from list
                    new_cards.pop()
        return False

    def backtracking2(self, cards: List[int]) -> bool:
        # using itertools - more compact code
        # base case
        if len(cards) == 1:
            return abs(cards[0] - 24.0) <= 0.01

        for a, b, *rest in permutations(cards):
            # iterate over every possible operation over pair
            for cur_num in self.generate_variants(num1=a, num2=b):
                rest.append(cur_num)
                # try new array
                if self.backtracking2(rest):
                    return True
                # if False - drop number from list
                rest.pop()
        return False

    def judgePoint24(self, cards: List[int]) -> bool:
        # 4! = 24 variants of numbers placing
        # 4^3 = 64 variants of of operators placing
        # 7 variants of parantheses placing
        # total 24*64*6 = 10752 variants
        # return self.backtracking(cards)  # accepted solution
        return self.backtracking2(cards)  # accepted solution
