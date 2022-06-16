"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution(object):
    
    def util(self, s):
        substr = ""
        max_len = 0

        for sym in s:

            if sym in substr:
                substr_len = len(substr)
                if substr_len > max_len:
                    max_len = substr_len
                sym_ind = substr.find(sym)
                substr = substr[sym_ind+1:]
                substr += sym
            else:
                substr += sym

        substr_len = len(substr)
        if substr_len > max_len:
            max_len = substr_len

        return max_len
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.util(s)
