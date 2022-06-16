"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        
        if len(strs) == 0:
            return prefix
        min_len = len(min(strs))
        
        if min_len == 0:
            return prefix
        i=0

        while i < min_len:
            c = strs[0][i]
            equal = all(a[i] == c for a in strs)
            #equal = len(set(map(lambda x: x[i], strs)))
            if equal == True:
                prefix += c
                i += 1
            else:
                break
        
        return prefix
