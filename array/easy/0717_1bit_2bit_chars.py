"""
717. 1-bit and 2-bit Characters

We have two special characters:

    The first character can be represented by one bit 0.
    The second character can be represented by two bits (10 or 11).

Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.

Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

Constraints:

    1 <= bits.length <= 1000
    bits[i] is either 0 or 1.
"""


class Solution:

    def bfs(self, bits: List[int]) -> bool:
        last_1_bit = False

        while bits:
            cur_bit = bits.pop(0)

            if cur_bit == 1:
                bits.pop(0)
                last_1_bit = False

            if cur_bit == 0:
                last_1_bit = True

        return last_1_bit

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        return self.bfs(bits)
