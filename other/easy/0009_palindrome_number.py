"""
9. Palindrome Number

Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. 
Therefore it is not a palindrome.

Follow up:

Coud you solve it without converting the integer to a string?
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        numbers = []

        if x < 0:
            return False
        elif x>=0 and x<10:
            return True
        else:
            cur_num = x
            while cur_num > 9:
                numbers.append(cur_num%10)
                cur_num = cur_num// 10
            numbers.append(cur_num)
        
        x_reversed = 0
        for ind in range(0, len(numbers)):
            x_reversed += numbers[ind] * 10**(len(numbers) - 1 - ind)
        print(x_reversed)
        if x_reversed == x:
            return True
        else:
            return False

