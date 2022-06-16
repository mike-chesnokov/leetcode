"""
38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. 
You can do so recursively, in other words from the previous member read off the digits, 
counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string. 

Example 1:
Input: 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" 
which means frequency = 1 and value = 2, the same way "1" is read as "11", 
so the answer is the concatenation of "12" and "11" which is "1211".
"""

class Solution:
    def my_count(self, string):
        # Runtime: 44 ms, faster than 20.88% of Python3 online submissions
        # Memory Usage: 13.8 MB, less than 74.15% of Python3 online submissions
        new_el = ""
        sym_cnt = 0
        el_len = len(string)
        for ind in range(el_len):
            cur_el = string[ind]
            sym_cnt += 1
            if ind + 1 == el_len:
                new_el += str(sym_cnt) + cur_el
                sym_cnt = 0
                break

            if cur_el != string[ind + 1]:
                new_el += str(sym_cnt) + cur_el
                sym_cnt = 0
        
        return new_el
    
    def my_count2(self, string):
        # Runtime: 40 ms, faster than 34.97% of Python3 online submissions
        # Memory Usage: 13.8 MB, less than 72.28% of Python3 online submissions
        new_el = ""
        sym_cnt = 0
        el_len = len(string)
        cur_el = string[0]

        for el in string:
            if el == cur_el:
                sym_cnt += 1
            else:
                new_el += str(sym_cnt) + cur_el
                sym_cnt = 1
                cur_el = el
        new_el += str(sym_cnt) + cur_el
        
        return new_el
    
    def countAndSay(self, n: int) -> str:        
        if n == 1:
            return "1"
        else:
            return self.my_count2(self.countAndSay(n-1))
