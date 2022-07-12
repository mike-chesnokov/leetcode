"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures,
 return an array answer such that answer[i] is the number of days you have to wait
 after the ith day to get a warmer temperature.
 If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100
"""
from typing import List


class Solution:

    def iterative(self, temperatures: List[int]) -> List[int]:
        """
        O(n^2) solution
        """
        result = []
        temp_len = len(temperatures)

        for ind1 in range(temp_len):
            found = False
            for ind2 in range(ind1 + 1, temp_len):
                if temperatures[ind2] > temperatures[ind1]:
                    result.append(ind2 - ind1)
                    found = True
                    break
            if not found:
                result.append(0)

        return result

    def iterative2(self, temperatures: List[int]) -> List[int]:
        result = [0]
        prev_stack = [temperatures[-1]]

        for temp in temperatures[-2::-1]:
            found = False
            for ind, prev_temp in enumerate(prev_stack[::-1], 1):
                if prev_temp > temp:
                    result.append(ind)
                    found = True
                    break
            if not found:
                result.append(0)
            prev_stack.append(temp)
        return result[::-1]

    def monotonic_stack(self, temperatures: List[int]) -> List[int]:
        """
        Iterate forward through the "temperatures" (until tempretures are decreasing)
        and move backward when we found a warmer day
        O(n) solution
        """
        temp_len = len(temperatures)
        result = [0] * temp_len
        # decreasing stack
        decr_stack = []

        for ind, temp in enumerate(temperatures):
            # print('*****************************')
            # print('ind =', ind, 'temp =', temp)
            # print('decr_stack =', decr_stack)

            while decr_stack and temp > decr_stack[-1][0]:
                prev_temp, prev_ind = decr_stack.pop()
                result[prev_ind] = ind - prev_ind
                # print('decr_stack =', decr_stack)
            decr_stack.append((temp, ind))
        return result

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # return self.iterative(temperatures) # Time Limit
        # return self.iterative2(temperatures) # Time Limit
        return self.monotonic_stack(temperatures)  # Accepted Solution
