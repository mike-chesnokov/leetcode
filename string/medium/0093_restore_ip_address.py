"""
93. Restore IP Addresses

A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

    For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
     but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits,
return all possible valid IP addresses that can be formed by inserting dots into s.
You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
    1 <= s.length <= 20
    s consists of digits only.
"""


class Solution:

    def __init__(self):
        self.result = []

    @staticmethod
    def insert_dot(string: str, ind: int) -> str:
        return string[:ind] + '.' + string[ind:]

    @staticmethod
    def get_ind_candidates(string: int) -> List[int]:
        """
        Return candidates from right dot to the end of string
        """
        string_len = len(string)
        # find the most right dot position
        right_dot_ind = string.rfind('.')

        # in case there is no dot
        if right_dot_ind == -1:
            start_ind = 1
        else:
            start_ind = right_dot_ind + 2
        # print("start_ind = ", start_ind)
        return [ind for ind in range(start_ind, string_len)]

    @staticmethod
    def is_valid(string: str) -> bool:
        for value in string.split('.'):

            if len(value) > 1 and value[0] == '0':
                return False

            if int(value) > 255:
                return False

        return True

    def backtracking(self, string: str) -> List[str]:
        """
        Bcktracking with dot position candidates
        """
        # ip has 3 dots
        if string.count('.') == 3 and self.is_valid(string):
            self.result.append(string)
            return

        # print("string = ", string)
        for ind in self.get_ind_candidates(string):
            # print("ind = ", ind)
            new_string = self.insert_dot(string, ind)
            # print("new_string = ", new_string)

            self.backtracking(new_string)

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.backtracking(s)
        return self.result
