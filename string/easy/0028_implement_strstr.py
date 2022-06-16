"""
28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? 
This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. 
This is consistent to C's strstr() and Java's indexOf().
"""

class Solution:
    
    def strStrSimple(self, haystack: str, needle: str) -> int:
        # Runtime: 36 ms, faster than 44.59% of Python3 online submissions
        # Memory Usage: 13.9 MB, less than 74.57% of Python3 online submissions
        
        len_needle = len(needle)
        
        if len_needle == 0:
            return 0

        for ind in range(len(haystack) - len_needle + 1):
            if needle == haystack[ind:ind + len_needle]:
                return ind
            
        return -1 
    
    def strStr(self, haystack: str, needle: str) -> int:
        return self.strStrSimple(haystack, needle)
