"""
0726. Number of Atoms

Given a string formula representing a chemical formula, return the count of each atom.
The atomic element always starts with an uppercase character, then zero or more lowercase letters,
representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1,
no digits will follow.

    For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.

Two formulas are concatenated together to produce another formula.

    For example, "H2O2He3Mg4" is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula.

    For example, "(H2O2)" and "(H2O2)3" are formulas.

Return the count of all elements as a string in the following form: the first name (in sorted order),
followed by its count (if that count is more than 1), followed by the second name (in sorted order),
followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.

Example 1:
Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.

Example 2:
Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:
Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
"""

from collections import defaultdict


class Solution:
    # cases:
    # "H" -> "H"
    # "H2" -> "H2"
    # "(H2O2)" -> "H2O2"

    """
    def parseWord(self, word: str) -> defaultdict(int):
        result_word = defaultdict(int)
        word_len = len(word)

        cur_start_ind = 0
        cur_end_ind = 1

        if cur_end_ind >= word_len:
            result_word[element_name] += 1
        else:
            while cur_end_ind < word_len + 1:
                #print('before', cur_start_ind, cur_end_ind, word[cur_start_ind: cur_end_ind], result_word)
                element_name = word[cur_start_ind: cur_end_ind]

                if cur_end_ind >= word_len or word[cur_end_ind].isupper():
                    result_word[element_name] += 1
                    cur_start_ind = cur_end_ind
                    cur_end_ind += 1

                elif word[cur_end_ind].isdigit():
                    result_word[element_name] += int(word[cur_end_ind])
                    cur_start_ind = cur_end_ind + 1
                    cur_end_ind += 2

                else:
                    cur_end_ind += 1

                #print('after', cur_start_ind, cur_end_ind, result_word)
        return result_word


    def countOfAtoms(self, formula: str) -> str:
        # part of recursive solution
        formula_len = len(formula)
        if formula_len == 1:
            return formula

        result_all = defaultdict(int)
        open_par_inds = []
        closed_par_inds = []

        for ind, symbol in enumerate(formula):
            if symbol == '(':
                open_par_inds.append(ind)
            if symbol == ')':
                closed_par_inds.append(ind)

        cnt_brackets = len(open_par_inds)
        if cnt_brackets > 0:
            for _ in range(cnt_brackets):
                print('before formula', formula)
                cur_start = open_par_inds.pop()
                cur_end = closed_par_inds.pop(0)
                temp = formula[cur_start + 1: cur_end]
                result_word = self.parseWord(temp)
                print('result_word', result_word)

                mult = 1

                if cur_end + 1 < formula_len:
                    if formula[cur_end + 1].isdigit():
                        mult = int(formula[cur_end + 1])
                        cur_end += 1

                for element in result_word:
                    result_all[element] += result_word[element] * mult

                formula = ''.join([
                            s for ind, s in enumerate(formula)
                            if ind < cur_start or ind > cur_end ])
                print('after formula', formula)

            if formula != '':
                result_word = self.parseWord(formula)
                for element in result_word:
                    result_all[element] += result_word[element]
        else:
            result_all = self.parseWord(formula)

        res_list = sorted(result_all.items(), key=lambda x: x[0])

        answer = ''

        for item in res_list:
            answer += item[0]
            if item[1] > 1:
                answer += str(item[1])

        return answer
        """

    def countOfAtoms(self, formula: str) -> str:
        # reverse iterate + digits in stack
        # reverse iterate + digits in stack
        result = defaultdict(int)  # dict to store counters of elements
        coef = 1  # default multiplier of element in brackets
        stack = []  # use stack to remember digit after brackets
        element_name = ""  # name of element
        digit_i = 0
        digit = 0

        for symbol in formula[::-1]:
            # print('*****************************')
            if symbol.isdigit():
                # for numbers with several digits
                digit += int(symbol) * (10 ** digit_i)
                digit_i += 1

            elif symbol == ')':
                stack.append(digit or 1)
                coef *= (digit or 1)
                digit, digit_i = 0, 0

            elif symbol == '(':
                coef = int(coef / stack.pop())  # return coef to previous value
                digit, digit_i = 0, 0

            elif symbol.isupper():
                element_name += symbol
                result[element_name[::-1]] += (digit or 1) * coef
                element_name = ""
                digit, digit_i = 0, 0

            elif symbol.islower():
                element_name += symbol

            # print('symbol = ', symbol)
            # print('digit_i = ', digit_i, 'digit = ', digit)
            # print('coef = ', coef)
            # print('stack = ', stack)
            # print('element_name = ', element_name)
            # print('result = ', result)

        res_list = sorted(result.items(), key=lambda x: x[0])

        answer = ''

        for item in res_list:
            answer += item[0]
            if item[1] > 1:
                answer += str(item[1])

        return answer
