"""
1200. Minimum Absolute Difference

Given an array of distinct integers arr,
find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
    a, b are from arr
    a < b
    b - a equals to the minimum absolute difference of any two elements in arr

Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:
Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
"""

from collections import defaultdict


class Solution:

    def bruteforce(self, arr: List[int]) -> List[List[int]]:
        """
        Check all possible pairs
        """
        arr_len = len(arr)
        # min_abs_diff_pairs: diff -> [(el1, el2), (el3, el4), ...]
        min_abs_diff_pairs = defaultdict(list)
        min_abs_diff = float("inf")

        for ind1 in range(arr_len):
            for ind2 in range(ind1 + 1, arr_len):
                arr_el1 = arr[ind1]
                arr_el2 = arr[ind2]
                # find diff
                diff = abs(arr_el1 - arr_el2)

                # save pair to list
                if arr_el1 > arr_el2:
                    min_abs_diff_pairs[diff].append((arr_el2, arr_el1))
                else:
                    min_abs_diff_pairs[diff].append((arr_el1, arr_el2))

                # update min abs diff
                if diff < min_abs_diff:
                    min_abs_diff = diff

        return sorted(min_abs_diff_pairs[min_abs_diff], key=lambda x: x[0], reverse=False)

    def sort_arr(self, arr: List[int]) -> List[List[int]]:
        """
        Sort array and check only consecutive pairs
        """
        arr_len = len(arr)
        arr_sorted = sorted(arr)
        # min_abs_diff_pairs: diff -> [(el1, el2), (el3, el4), ...]
        min_abs_diff_pairs = defaultdict(list)
        min_abs_diff = float("inf")

        for ind in range(arr_len - 1):
            # find diff
            diff = arr_sorted[ind + 1] - arr_sorted[ind]
            # save pair to list
            min_abs_diff_pairs[diff].append((arr_sorted[ind], arr_sorted[ind + 1]))

            # update min abs diff
            if diff < min_abs_diff:
                min_abs_diff = diff

        return min_abs_diff_pairs[min_abs_diff]

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # return self.bruteforce(arr)
        return self.sort_arr(arr)