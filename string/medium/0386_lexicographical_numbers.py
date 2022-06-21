"""
386. Lexicographical Numbers

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.

Example 1:
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:
Input: n = 2
Output: [1,2]
"""
import bisect
from typing import List


class Solution:

    def built_in_sort(self, n: int) -> List[int]:
        arr = [str(ind) for ind in range(1, n + 1)]
        arr = sorted(arr)
        return arr

    def binary_insert(self, n: int) -> List[int]:
        arr = []

        for el in range(1, n + 1):
            bisect.insort_left(arr, str(el))
        return arr

    def lexicalOrder(self, n: int) -> List[int]:
        # return self.built_in_sort(n)  # accepted solution
        return self.binary_insert(n)  # accepted solution
