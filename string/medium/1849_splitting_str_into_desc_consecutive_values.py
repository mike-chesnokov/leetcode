"""
1849. Splitting a String Into Descending Consecutive Values

You are given a string s that consists of only digits.

Check if we can split s into two or more non-empty substrings such
that the numerical values of the substrings are in descending order
and the difference between numerical values of every two adjacent substrings is equal to 1.

    For example, the string s = "0090089" can be split into ["0090", "089"] with numerical values [90,89].
    The values are in descending order and adjacent values differ by 1, so this way is valid.
    Another example, the string s = "001" can be split into ["0", "01"], ["00", "1"], or ["0", "0", "1"].
    However all the ways are invalid because they have numerical values [0,1], [0,1], and [0,0,1] respectively,
    all of which are not in descending order.

Return true if it is possible to split s as described above, or false otherwise.

A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "1234"
Output: false
Explanation: There is no valid way to split s.

Example 2:
Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.

Example 3:
Input: s = "9080701"
Output: false
Explanation: There is no valid way to split s.
"""
from typing import List

class Solution:
    memo = {}  # store checks for repeating splits

    def check_arr(self, arr: List[str]) -> bool:
        if tuple(arr) in self.memo:
            print(arr, 'memo')
            return self.memo[tuple(arr)]

        print(arr)

        if len(arr) == 1:
            self.memo[tuple(arr)] = False
            return False

        for ind in range(len(arr) - 1):
            if int(arr[ind]) - int(arr[ind + 1]) != 1:
                self.memo[tuple(arr)] = False
                return False

        self.memo[tuple(arr)] = True
        return True

    def brute_force(self, arr: List[str]) -> bool:
        # check current sequense
        if self.check_arr(arr):
            return True

        # split every element of array
        for ind1, el in enumerate(arr):
            for ind2 in range(1, len(el)):
                # if we can split el - do it
                if len(el) > 1:
                    # create new array without old element
                    # split element into 2
                    # add 2 elements to new array
                    new_arr = [substr for ind, substr in enumerate(arr)
                               if ind != ind1]
                    new_arr.insert(ind1, el[:ind2])
                    new_arr.insert(ind1 + 1, el[ind2:])

                    # repeat for new array
                    if self.brute_force(new_arr):
                        return True
        return False

    def backtracking(self, s: str, prev_num: int = None) -> bool:
        # print(s)
        # base case
        if prev_num and prev_num - int(s) == 1:
            return True
        # split string and check current number
        for ind in range(1, len(s)):
            cur_num = int(s[:ind])
            #  compare current and previous numbers
            if prev_num is None or prev_num - cur_num == 1:
                if self.backtracking(s[ind:], cur_num):
                    return True
        return False

    def splitString(self, s: str) -> bool:
        # cut leading zeros in the initial string
        for ind in range(len(s)):
            if s[ind] != "0":
                # return self.brute_force([s[ind:]])  # time limit
                return self.backtracking(s[ind:], None)  # accepted solution
        return False
