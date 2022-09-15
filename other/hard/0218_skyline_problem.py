"""
218. The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city
when viewed from a distance.
Given the locations and heights of all the buildings,
return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings
where buildings[i] = [lefti, righti, heighti]:
    lefti is the x coordinate of the left edge of the ith building.
    righti is the x coordinate of the right edge of the ith building.
    heighti is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate
in the form [[x1,y1],[x2,y2],...].
Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list,
which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends.
Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline.
For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable;
 the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]


Example 1:
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.

Example 2:
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]

Constraints:
    1 <= buildings.length <= 104
    0 <= lefti < righti <= 231 - 1
    1 <= heighti <= 231 - 1
    buildings is sorted by lefti in non-decreasing order.
"""

import bisect
from collections import defaultdict
from typing import List


class Solution:

    def brute_force(self, buildings: List[List[int]]) -> List[List[int]]:
        result = []
        max_heights = defaultdict(int)
        max_right = 0
        min_left = buildings[0][0]

        # process all buildings
        for left, right, height in buildings:
            for ind in range(left, right):
                # save max heights
                if height > max_heights[ind]:
                    max_heights[ind] = height

                if right > max_right:
                    max_right = right
        # print('max_heights = ', max_heights)

        # compute output
        prev_height = 0
        for ind in range(min_left, max_right + 1):
            cur_height = max_heights[ind] if ind in max_heights else 0
            # print('ind = ', ind, 'cur_height = ', cur_height, 'prev_height = ', prev_height)
            if cur_height != prev_height:
                result.append([ind, cur_height])
            prev_height = cur_height

        return result

    def priority_queue(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        Use bisect to create pq with max heigth at the end
        From https://leetcode.com/problems/the-skyline-problem/discuss/325070/Simple-Python-solutions/777916
        """
        # process buildings
        points = []  # [(x_coord, height, point_type)]
        for start, end, height in buildings:
            points.append((start, -height, 0))  # point_type=0 - left corner of building
            points.append((end, height, 1))  # point_type=1 - right corner of building
        # print('points = ', points)
        points.sort()
        # print('points = ', points)

        result = []
        prev_height = 0
        pq = [0]

        for position, height, point_type in points:
            # print('position = ', position, 'height = ', height, 'point_type = ', point_type)
            # print('pq = ', pq)
            if point_type == 0:  # if left corner of building
                bisect.insort_right(pq, -height)
            else:  # if right corner of building
                pq.pop(bisect.bisect_left(pq, height))
            # print('pq = ', pq)

            cur_height = pq[-1]  # max height always at the end of pq

            if prev_height != cur_height:
                result.append((position, cur_height))
                prev_height = cur_height
            # print('result = ', result)
        return result

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # return self.brute_force(buildings)  # Time limit
        return self.priority_queue(buildings)  # Accepted
