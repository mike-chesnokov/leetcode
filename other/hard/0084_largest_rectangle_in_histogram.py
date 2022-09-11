"""
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
    1 <= heights.length <= 105
    0 <= heights[i] <= 104
"""
from typing import List


class Solution:

    def brute_forse(self, heights: List[int]) -> int:
        """
        Brute force O(n^3) solution
        """
        heights_len = len(heights)
        max_area = 0

        for start_ind in range(heights_len):
            for end_ind in range(start_ind + 1, heights_len + 1):
                # calcualte current height (cur_min) and width (cur_len)
                cur_len = len(heights[start_ind:end_ind])
                cur_min = min(heights[start_ind:end_ind])
                # calculate area
                cur_area = cur_len * cur_min

                # print('*********************************')
                # print('start_ind = ', start_ind,'end_ind = ', end_ind)
                # print('heights[start_ind:end_ind] = ', heights[start_ind:end_ind])
                # print('cur_len = ', cur_len, 'cur_min =', cur_min)

                # compare with max_area
                if cur_area > max_area:
                    max_area = cur_area
        return max_area

    def brute_forse2(self, heights: List[int]) -> int:
        """
        Brute force O(n^2) solution
        """
        heights_len = len(heights)
        max_area = 0

        for start_ind in range(heights_len):
            cur_min = heights[start_ind]
            for end_ind in range(start_ind + 1, heights_len + 1):
                # calcualte current height (cur_min) and width (cur_len)
                cur_len = len(heights[start_ind:end_ind])
                # calculate current min
                temp = heights[end_ind - 1]
                if temp < cur_min:
                    cur_min = temp
                # calculate area
                cur_area = cur_len * cur_min

                # print('*********************************')
                # print('start_ind = ', start_ind,'end_ind = ', end_ind)
                # print('heights[start_ind:end_ind] = ', heights[start_ind:end_ind])
                # print('cur_len = ', cur_len, 'cur_min =', cur_min)

                # compare with max_area
                if cur_area > max_area:
                    max_area = cur_area
        return max_area

    def divide_conquer1(self, heights: List[int]) -> int:
        heights_len = len(heights)
        # basic case
        if heights_len == 0:
            return 0

        # find the current min
        min_height = float("+inf")
        min_ind = 0
        for ind, height in enumerate(heights):
            if height < min_height:
                min_height = height
                min_ind = ind

        # compute current area
        cur_area = min_height * heights_len

        # go to the left and right subarrays
        left_area = self.divide_conquer1(heights[:min_ind])
        right_area = self.divide_conquer1(heights[min_ind + 1:])
        return max(cur_area, left_area, right_area)

    def divide_conquer2(self, heights: List[int]) -> int:
        """
        From https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/1419073/Python-Divide-and-Conquer
        """
        if not heights:
            return 0
        bottom = min(heights)
        length = len(heights)
        bottom_max = bottom * length
        prev = 0
        subs = []
        for i in range(length):
            if heights[i] == bottom:
                subs.append(heights[prev:i])
                prev = i + 1
        subs.append(heights[prev:])
        return max([self.divide_conquer2(sub) for sub in subs] + [bottom_max])

    def left_right_arrays(self, heights: List[int]) -> int:
        """
        From https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28963/Python-solution-without-using-stack.-(with-explanation)

        left[i], right[i] represent how many bars are >= than the current bar
        """
        heights_len = len(heights)
        left = [1] * heights_len
        right = [1] * heights_len

        # calculate left distances
        for i in range(0, heights_len):
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                j -= left[j]  # use already calculated distances
            left[i] = i - j

        # calculate right distances
        for i in range(heights_len - 2, -1, -1):
            j = i + 1
            while j < heights_len and heights[j] >= heights[i]:
                j += right[j]  # use already calculated distances
            right[i] = j - i

        max_area = 0
        for i in range(0, heights_len):
            max_area = max(max_area, heights[i] * (left[i] + right[i] - 1))

        return max_area

    def monotonic_stack(self, heights: List[int]) -> int:
        """
        Using increasing stack - values saved in increasing order.
        """
        max_area = 0
        stack = [(-1, 0)]  # [(ind, height)]
        heights = heights + [0]  # for full stack processing at the end

        for ind, height in enumerate(heights):
            # print('************************')
            # print('ind = ', ind,'height = ', height)
            # print('stack = ', stack)

            while height < stack[-1][1]:
                prev_ind, prev_height = stack.pop()
                # print('prev_ind = ', prev_ind,'prev_height = ', prev_height)
                # print('stack[-1] = ', stack[-1])
                cur_area = (ind - stack[-1][0] - 1) * prev_height
                max_area = max(max_area, cur_area)
                # print('cur_area = ', cur_area,'max_area = ', max_area)

            stack.append((ind, height))

        # print('----------------')
        # print('stack = ', stack)

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        # return self.brute_forse(heights)  # Time Limit
        # return self.brute_forse2(heights)  # Time Limit
        # return self.divide_conquer1(heights)  # Memory Limit
        # return self.divide_conquer2(heights)  # Time Limit
        # return self.left_right_arrays(heights)  # Accepted
        return self.monotonic_stack(heights)  # Accepted
