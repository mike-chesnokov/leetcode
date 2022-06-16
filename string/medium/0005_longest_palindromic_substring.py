"""
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    
    def findPalindromeLength(self, s, input_len, left_ind, right_ind) -> int:
        # print('find input', left_ind, right_ind)
        # iterate while there is symmetry around center
        # return final pal
        pal = ''
        while left_ind >= 0 and right_ind < input_len and s[left_ind] == s[right_ind]:
            # print('find', left_ind, right_ind, s[left_ind : right_ind + 1])
            pal = s[left_ind : right_ind + 1]
            left_ind -= 1
            right_ind += 1

        # print('return', pal)
        return pal 
    
    def twoSidesSymmetry(self, s: str) -> str:
        # Runtime: 1352 ms, faster than 56.23% of Python3 online submissions
        # Memory Usage: 13.7 MB, less than 88.70% of Python3 online submissions
        # for every element look at 2 cases: even and odd num sumbols palindroms
        input_len = len(s)
        
        if input_len <= 1:
            return s
        
        max_pal = ''
        
        # iterate over string
        for ind in range(input_len):                  
            max_pal_len = len(max_pal)  
            # print(ind, s[ind], max_pal_len)
            
            # find palindromes for 2 cases
            two_sym_pal = self.findPalindromeLength(s, input_len, ind, ind)
            three_sym_pal = self.findPalindromeLength(s, input_len, ind, ind + 1)
            
            # ipdate max length palindrome
            if len(two_sym_pal) > max_pal_len:
                max_pal = two_sym_pal
                
            if len(three_sym_pal) > max_pal_len:
                max_pal = three_sym_pal
                
            # print('2:', two_sym_pal, '3:', three_sym_pal, 'max: ', max_pal)
            
        return max_pal
    
    def longestPalindrome(self, s: str) -> str:
        return self.twoSidesSymmetry(s)
